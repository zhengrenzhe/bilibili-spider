import psycopg2

from utils.cfg import get_cfg

CONN = psycopg2.connect(
    dbname="bilibili",
    user="postgres",
    password="1234",
    host=get_cfg("postgres.host"),
    port=get_cfg("postgres.port")
)
CUR = CONN.cursor()
