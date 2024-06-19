import sqlite3 
con = None
cur = None

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def init():
    global con, cur
    con = sqlite3.connect("recipes.db")
    con.row_factory = dict_factory
    cur = con.cursor()


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
    cur.executemany(f"INSERT INTO {table_name} {column_names} VALUES {placeholders}", values)
    con.commit()


# {"table_name": [{"col1": val1, "col2": val2}] } etc
def get_value(data):
    table_name, columns, values = deconstruct(data)
    if len(values) != 1:
        return None
    condition_string = "AND ".join([ f"{col} = ?" for col in columns])
    print(condition_string, values)
    cur.execute(f"SELECT * FROM {table_name} WHERE {condition_string}", values[0])
    return cur.fetchone()


if __name__ == "__main__":
    init()
    print(get_value({"recipe": [{"id": 1}]}))
    
