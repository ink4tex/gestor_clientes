from sqlite3 import connect
import psycopg2
import psycopg2.extras
from schema import instructions

connect = psycopg2.connect(host = 'localhost', database = 'gestor_clientes', user = 'postgres', password = '123456')
cursor = connect.cursor(cursor_factory=psycopg2.extras.DictCursor)

for i in instructions:
    cursor.execute(i)
connect.commit()
