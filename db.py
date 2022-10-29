# -*- coding: utf-8 -*-
"""Supabase (database) module

This module create the supabase client object, and insert or update rows of
the postgres database.

Todo:
    *For modules TODOs
"""

from supabase import create_client, Client
from dotenv import load
import os

# Load .env variables
load()
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
SUPABASE_SECRET_KEY = os.getenv('SUPABASE_SECRET_KEY')


def modify_db(food_data: dict, supabase: Client, date_exists: str) -> None:
    """Insert or update a supabase database row

    Args:
        food_data (dict): The database row data in the form of a dictionary
        supabase (supabase.Cliente): the supabase client
        date_exists (str): The date (as a string) if this already exists in the DB

    Return:
        None

    Todo:
        * Change food_date to a List, to modify several rows at the same time
    """
    
    if date_exists:
        row = supabase.table('feeding').update(food_data).eq('date', food_data['date']).execute()
    else:
        row = supabase.table('feeding').insert(food_data).execute()


def get_db(supabase: Client, date: str):
    row = supabase.table('feeding').select('*').eq('date', date).execute()
    return row


def get_supabase() -> Client:
    """Get the supabase client

    Args:
        None

    Return:
        supabase.Client

    Todo:
        * implement supabase url and supabase key as argument insted of general variables
        * Use a try/except block
    """
    return create_client(SUPABASE_URL, SUPABASE_KEY)
