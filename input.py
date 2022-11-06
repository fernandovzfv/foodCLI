# -*- coding: utf-8 -*-
# input.py
"""Funtions to manage user inputs

Functions:
- get_user_input: _
- input_feeding: _
- input_general_params: _
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
