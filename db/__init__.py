import psycopg2

_conn = psycopg2.connect(dbname="bilibili", user="postgres", password="1234", host="127.0.0.1")
_cur = _conn.cursor()
