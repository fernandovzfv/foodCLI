# -*- coding: utf-8 -*-

import unittest
import os
from dotenv import load_dotenv
from db import get_supabase, modify_data
from datetime import date

load_dotenv(dotenv_path='test.env')

class TestSupabase(unittest.TestCase):
    def test_supabase(self):
        url = os.environ.get('SUPABASE_TEST_URL')
        assert url is not None, "Must provide SUPERBASE_TEST_URL environment variable"
        key = os.environ.get('SUPABASE_TEST_KEY')
        assert key is not None, "Must provide SUPERBASE_TEST_KEY environment variable"
        return get_supabase(url, key)

    def test_modify_data(self):
        _ = date.today()
        current_date = str(_.day) + '-' + str(_.month) + '-' + str(_.year)
        food_data = {'date': current_date, 'x_var': 4, 'notes': 'testing'}
        date_exists = False
        table = 'testing'
        url = os.environ.get('SUPABASE_TEST_URL')
        key = os.environ.get('SUPABASE_TEST_KEY')
        supabase = get_supabase(url, key)
        row = modify_data(food_data, supabase, date_exists, table)
        assert len(row.data) == 1, "Error inserting data to DB"



if __name__ == '__main__':
    unittest.main()
