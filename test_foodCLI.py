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
        self.assertIsNotNone(url)
        key = os.environ.get('SUPABASE_TEST_KEY')
        self.assertIsNotNone(key)
        return get_supabase(url, key)

    def test_modify_data(self):
        """Test de modify_data function

        TODO: Correct that the information is duplicated in feeding and testing table after run test.
        """
        _ = date.today()
        current_date = str(_.day) + '-' + str(_.month) + '-' + str(_.year)
        food_data = {'date': current_date, 'x_var': 4, 'notes': 'testing'}
        date_exists = False
        table = 'testing'
        url = os.environ.get('SUPABASE_TEST_URL')
        key = os.environ.get('SUPABASE_TEST_KEY')
        supabase = get_supabase(url, key)
        row = modify_data(food_data, supabase, date_exists, table)
        self.assertEqual(len(row.data), 1)


if __name__ == '__main__':
    unittest.main()
