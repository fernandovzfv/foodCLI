# -*- coding: utf-8 -*-
"""Supabase (database) module

This module create the supabase client object, and insert or update rows of
the postgres database.

Todo:
    *For modules TODOs
"""

from supabase import create_client, Client


def modify_data(food_data: dict, supabase: Client, date_exists: str, table: str) -> None:
    """Insert or update a supabase database row

    Args:
        food_data (dict): The database row data in the form of a dictionary
        supabase (supabase.Cliente): the supabase client
        date_exists (str): The date (as a string) if this already exists in the DB
        table (str): Table name to modify

    Return:
        None

    Todo:
        * Change food_date to a List, to modify several rows at the same time
    """
    
    if date_exists:
        row = supabase.table(table).update(food_data).eq('date', food_data['date']).execute()
    else:
        row = supabase.table(table).insert(food_data).execute()
    
    return row


def get_data(supabase: Client, date: str, table: str):
    """_summary_

    Args:
        supabase (Client): _description_
        date (str): _description_
        table (str, optional): _description_. Defaults to 'feeding'.

    Returns:
        _type_: _description_
    """
    row = supabase.table(table).select('*').eq('date', date).execute()
    return row


def get_supabase(url: str, key: str) -> Client:
    """Get the supabase client

    Args:
        None

    Return:
        supabase.Client

    Todo:
        * implement supabase url and supabase key as argument insted of general variables
        * Use a try/except block
    """
    return create_client(url, key)
