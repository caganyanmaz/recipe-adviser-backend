import time
import os
import sqlite3 
from threading import Lock
con = None
cur = None
lock = None

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def init():
    global con, cur, lock
    con = sqlite3.connect("recipes.db", check_same_thread=False)
    con.row_factory = dict_factory
    cur = con.cursor()
    lock = Lock()


def get_instructions_of_recipe(recipe_id):
    print(recipe_id)
    lock.acquire(True)
    cur.execute("SELECT * FROM instruction_recipe WHERE recipe_id = ? ORDER BY ord ASC", (recipe_id, ))
    res = cur.fetchall()
    lock.release()
    return res


def deconstruct(data):
    table_name = list(data.keys())[0]
    if data[table_name] == 0:
        return (table_name, (), [])
    columns = tuple(list(data[table_name][0].keys()))
    values = [ tuple([row[col] for col in columns]) for row in data[table_name] ]
    return table_name, columns, values


def insert_values(data):
    table_name, columns, values = deconstruct(data)
    if len(values) == 0:
        return
    column_names = "(" + ", ".join(columns) + ")"
    placeholders = "(" + ", ".join(["?"] * len(columns)) + ")"
    lock.acquire(True)
    cur.executemany(f"INSERT INTO {table_name} {column_names} VALUES {placeholders}", values)
    con.commit()
    lock.release()


def get_values(data):
    table_name, columns, values = deconstruct(data)
    lock.acquire(True)
    execute_select_query(table_name, columns, values)
    res = cur.fetchall()
    lock.release()
    return res


def get_value(data):
    table_name, columns, values = deconstruct(data)
    lock.acquire(True) 
    execute_select_query(table_name, columns, values)
    res = cur.fetchone()
    lock.release()
    return res


def execute_select_query(table_name, columns, values):
    if len(values) != 1:
        return None
    condition_string = "AND ".join([ f"{col} = ?" for col in columns])
    cur.execute(f"SELECT * FROM {table_name} WHERE {condition_string}", values[0])


if __name__ == "__main__":
    init()
    print(get_value({"recipe": [{"id": 1}]}))
    
