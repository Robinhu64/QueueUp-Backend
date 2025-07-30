import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()



def start_db():
    # Connect to the School database
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres.pvqsqlnhxougmknlboko",
        password=os.getenv("DATA_BASE_KEY"),
        host="aws-0-eu-west-3.pooler.supabase.com"
    )
    cur = conn.cursor()
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)