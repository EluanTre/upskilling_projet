#!/home/lrcom/data_upskilling/upskilling_projet/.venv/bin/python3
import duckdb
import pandas as pd
import streamlit as st

from database import init_database

DB_PATH = 'data/database.duckdb'

with duckdb.connect(DB_PATH) as conn:

    pass
    