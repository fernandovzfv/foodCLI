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

from csv import excel
import time
import supabase
import typer
from dotenv import load_dotenv
import os
from db import get_supabase, modify_data, get_data
"""Import supabase client from db.py

get_supabase: return supabase.Client object
modify_db: insert or update database row
"""

from input import get_user_input, input_feeding, input_general_params

# Load .env variables
load_dotenv()
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
SUPABASE_SECRET_KEY = os.getenv('SUPABASE_SECRET_KEY')


def main(param: str):
    """Register of food ingestion.
Use
    params: breakfast, lunch, dinner, general, get, and insert.
    """

    print("<<FOOD REGISTER>>")

    supabase = get_supabase(SUPABASE_URL, SUPABASE_KEY)
    while True:
        current_date = input('Input the date (dd-mm-yyyy): ')
        try:
            valid_date = time.strptime(current_date, '%d-%m-%Y')
            break
        except ValueError:
            print('Invalid format date!')
            continue

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
        modify_data(food_data, supabase, date_exists, 'feeding')
        print(f'Food: {food_data}')

    elif param == 'insert':
        print('[' + param + ']')
        new_data = {}
        for meal in meals:
            new_data.update(input_feeding(meal, current_date, current_info))
        new_data.update(input_general_params(current_date, current_info))
        modify_data(new_data, supabase, date_exists, 'feeding')
        print(new_data)
    
    elif param == 'general':
        print('[' + param + ']')
        params = input_general_params(current_date, current_info)
        modify_data(params, supabase, date_exists, 'feeding')
        print(f'General params: {params}')

    elif param == 'get':
        print('[' + param + ']')
        print(get_data(supabase, current_date))
    
    else:
        print(f'Unknown option: {param}')
        print('Use "python food.py --help" to help')


if __name__ == '__main__':
    typer.run(main)
