# foodCLI
Version 0.1.0

## Description
This application is a script to register in a PostgreSQL database in [Supabase](https://supabase.com/) some parameters regarding food ingestion and other variables that could affect your health.

The idea behind this simple application is to control an X-Variable (i.e., high blood pressure, gastritis, etc.) in the function of food ingestion.

We'll register the following parameters:

- Foof ingestion at breakfast, lunch, and diner (until five meals)
- General parameters
  - Sugar intake scale
  - Spicy consumption scale
  - Stressful scale
  - sleeping hours
  - resting hours
  - X-variable scale


## Script description
This is a python script using these libraries:

- [Typer](https://github.com/tiangolo/typer)
- [Supabase-py](https://github.com/supabase-community/supabase-py)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

## Usage:

`$ python foodCLI.py --help` for reference

## TODO

- Input data verification
- Completing this document

## Table columns

| column_name | data_type |
| ----------- | --------- |
| x_var       | smallint  |
| notes       | text      |
| b_m1        | text      |
| b_m2        | text      |
| b_m3        | text      |
| b_m4        | text      |
| b_m5        | text      |
| b_sl        | integer   |
| b_pl        | integer   |
| l_m1        | text      |
| l_m2        | text      |
| l_m3        | text      |
| l_m4        | text      |
| l_m5        | text      |
| l_sl        | integer   |
| l_pl        | integer   |
| d_m1        | text      |
| d_m2        | text      |
| d_m3        | text      |
| d_m4        | text      |
| d_m5        | text      |
| d_sl        | integer   |
| d_pl        | integer   |
| s_level     | integer   |
| sleep       | integer   |
| rest        | integer   |
| date        | text      |
| id          | integer   |
