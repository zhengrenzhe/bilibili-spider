import psycopg2

CONN = psycopg2.connect(dbname="bilibili", user="postgres", password="1234", host="postgres-service")
CUR = CONN.cursor()

from infrastructure.postgres import video, author
