import psycopg2

CONN = psycopg2.connect(dbname="bilibili", user="postgres", password="1234", host="127.0.0.1")
CUR = CONN.cursor()

from infrastructure.postgres import video, author
