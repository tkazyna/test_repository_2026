import psycopg2
from config import config

def get_connection():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка подключения к базе:", error)
        return None