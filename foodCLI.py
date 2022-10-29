# -*- coding: utf-8 -*-
"""CLI to register food consumption.

This program read from the user the food consuption,
and save these data to a Postgres database in supabase.
Example:
    $ python foodCLI.py [Options]

Options:
    - breakfast: until 5 foods + suggar scale + hot scale
    - lunch: until 5 foods + suggar scale + hot scale
    - dinner: until 5 foods + sugar scale + hot scale
    - general: Stressful scale + sleeping hours + resting hours
    - notes: Notes + X-variable (to control; i.e., stomach acidity)

Scales:
    - 1: Very low scale or none
    - 2: Low scale
    - 3: high scale
    - 4: Very high scale
"""

import supabase
import typer
from db import get_supabase, modify_db, get_db
"""Import supabase client from db.py

get_supabase: return supabase.Client object
modify_db: insert or update database row
"""


def get_user_input(db_column: str, question: str, current_info: dict) -> str:
    """Prepare the question for user, and read the anwer

    Args:
        db_column (str): database column name
        question (str): question to ask
        current_info (dict): existing database row or {} if none

    Returns:
        str: answer of the user.
    """
    
    if current_info:
        current_value = current_info[db_column]
        question = question + " [" + str(current_value) + "]: "
    else:
        question = question + ": "
    
    answer = input(question)
    if answer:
        return answer
    else:
        if current_info:
            return current_info[db_column]
        else:
            return ''


def input_feeding(meal: str, current_date: str, current_info: dict) -> dict:
    """Read the food ingestion to breakfast, lunch, or dinner

    Args:
        meal (str): It could be breakfast, lunch or dinner
        current_date (str): date to register in the format "dd-mm-yyyy"
        current_info (dict): existing database row or {} if none
    
    Return:
        dict: database row information to register (partial)
    """
    char = meal[:1]
    food = {}
    food['date'] = current_date
    print('[' + meal + ']')
    # read information
    for i in range(5):
        column_db = char + '_m' + str(i+1)
        meal = get_user_input(column_db, f"Describe meal No. {i+1}", current_info)
        if meal:
            food[column_db] = meal
        else:
            break
    
    column_db = char + '_sl'
    sweety_scale = get_user_input(column_db, "Sweety scale (1-4)", current_info)
    food[column_db] = int(sweety_scale)
    
    column_db = char + '_pl'
    hot_scale = get_user_input(column_db, "Hot scale (1-4)", current_info)
    food[column_db] = int(hot_scale)
    
    return food


def input_general_params(current_date: str, current_info: dict) -> dict:
    """Read the stressful scale, sleeping and resting hours,
       x-variable scale, and notes

    Args:
        current_date (str): date to register in the format "dd-mm-yyyy"
        current_info (dict): existing database row or {} if none
    
    Return:
        dict: database row information to register (partial)
    """

    params = {}
    params['date'] = current_date
    
    params['s_level'] = int(get_user_input('s_level',
                                           'Input stressful scale (1-4)',
                                           current_info))
    params['sleep'] = int(get_user_input('sleep',
                                         'Input sleeping hours',
                                         current_info))
    params['rest'] = int(get_user_input('rest',
                                        'Input resting hours',
                                        current_info))
    params['x_var'] = int(get_user_input('x_var',
                                        'Input X-variable value (1-4)',
                                        current_info))
    params['notes'] = get_user_input('notes',
                                     'Input your comments',
                                     current_info)
    
    return params


def main(param: str):
    """Register of food ingestion.
Use
    params: breakfast, lunch, dinner, general, get, and insert.
    """

    print("<<FOOD REGISTER>>")

    supabase = get_supabase()
    current_date = input('Input the date?: ')
    info_dict = supabase.table('feeding').select('*').eq('date', current_date).execute().data
    if info_dict:
        current_info = info_dict[0]
        date_exists = current_info['date']
    else:
        current_info = {}
        date_exists = ''
    
    meals = ['breakfast', 'lunch', 'dinner']
    if param in meals:
        print('[Food]')
        food_data = input_feeding(param, current_date, current_info)
        modify_db(food_data, supabase, date_exists)
        print(f'Food: {food_data}')

    elif param == 'insert':
        print('[' + param + ']')
        new_data = {}
        for meal in meals:
            new_data.update(input_feeding(meal, current_date, current_info))
        new_data.update(input_general_params(current_date, current_info))
        modify_db(new_data, supabase, date_exists)
        print(new_data)
    
    elif param == 'general':
        print('[' + param + ']')
        params = input_general_params(current_date, current_info)
        modify_db(params, supabase, date_exists)
        print(f'General params: {params}')

    elif param == 'get':
        print('[' + param + ']')
        print(get_db(supabase, current_date))
    
    else:
        print(f'Unknown option: {param}')
        print('Use "python food.py --help" to help')


if __name__ == '__main__':
    typer.run(main)
