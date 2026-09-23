import psycopg 
import pytest


def test_post_connection():
    conn = psycopg.connect("dbname=jack")
    with psycopg.connect("dbname=jack") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
            assert cur.fetchone()[0] == 1