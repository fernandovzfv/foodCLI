# -*- coding: utf-8 -*-
"""Supabase (database) module

This module create the supabase client object, and insert or update rows of
the postgres database.

Todo:
    *For modules TODOs
"""


from supabase import create_client, Client

# TODO: Use a .env file and python-dotenv module, instead of hard code keys.
SUPABASE_URL = 'https://uufezkbamnwbweoqrsnq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV1ZmV6a2JhbW53Yndlb3Fyc25xIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjQ5NzExNjAsImV4cCI6MTk4MDU0NzE2MH0.9vqdTlk14X2Ii1vT0czg6_0dtQTIW7KXtcNpjRUGfMc'
SUPABASE_SECRET_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV1ZmV6a2JhbW53Yndlb3Fyc25xIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY2NDk3MTE2MCwiZXhwIjoxOTgwNTQ3MTYwfQ.PjJi_l79tNRFlAgZN1u9Qk7vEyvoZ7l5uZSz_cSRVwk'


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
