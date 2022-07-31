from email import headerregistry
from tkinter.tix import Tree
import psycopg2
from pyparsing import str_type

conn = psycopg2.connect("postgresql://brayton:51gSHp3yJ9LrRY7ox0lbTw@free-tier6.gcp-asia-southeast1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dpurer-oriole-3004")

STR_TYPE = 'VARCHAR(60)'
LINK_TYPE = 'VARCHAR(600)'
INT_TYPE = 'INT'

headers = []
header_types = []
table = ""

def setHeaders(param):
    global headers
    headers = param

def setHeaderTypes(param):
    global header_types
    header_types = param

def setTable(param):
    global table
    table = param

def create_table(table_name=table, fields=headers, field_types=header_types, commit=True):
    if not fields or not field_types or not table_name:
        fields, field_types, table_name = headers, header_types, table
    if len(fields) != len(field_types): return
    parameters = ', '.join([' '.join([fields[i], field_types[i]]) for i in range(len(fields))])

    with conn.cursor() as cur:
        cur.execute(
            f'create table if not exists {table_name} ({parameters})'
        )
        
    if commit: conn.commit()
    else: print(parameters)
    
def drop_table(table_name=table):
    if not table_name: table_name = table
    with conn.cursor() as cur: 
        cur.execute(
            f"drop table {table_name}"
        )
        
    conn.commit()
    
def upsert_one(single_item, table_name=table, fields=headers, commit=True):
    # single item is sent as a json dictionary with the headers
    if not fields or not table_name:
        fields, table_name = headers, table
    header_parameters = ", ".join(header_types)
    values_parameters = ', '.join([f"'{single_item.get(key, '')}'" for key in fields])
    if not commit: print(header_parameters, '/n', values_parameters)
    
    with conn.cursor() as cur: 
        cur.execute(
            f"upsert into {table_name} values ({values_parameters})"
        )
        
    if commit: conn.commit()

def upsert_many(items, table_name=table, fields=headers, commit=True):
    # items come in [{},{},{}] arr of dict
    for item in items:
        upsert_one(item, table_name=table_name, fields=fields, commit=commit)
    
def delete_where(condition, table_name=table, commit=True):
    if not table_name: table_name = table
    with conn.cursor() as cur: 
        cur.execute(
            f"delete from {table_name} where {condition}"
        )
        
    if commit: conn.commit()
    else: print(f"delete from {table_name} where {condition}")
    
def get_condition(field, value):
    return f"{field} = '{value}'"

def get_all_as_dict(results, fields=headers):
    if not fields: fields = headers
    arr = []
    for each in results:
        doc = {}
        for i in range(len(fields)):
            field = fields[i]
            doc[field] = each[i]
        arr.append(doc)
    return arr

def get_items(table_name=table, fields=headers):
    if not table_name: table_name = table
    with conn.cursor() as cur:
        cur.execute(
            f"SELECT * FROM {table_name}"
        )
        
        # a list of tuples
        result = cur.fetchall()
        return get_all_as_dict(result, fields)
        
def get_items_where(condition, table_name=table, fields=headers):
    if not table_name: table_name = table
    with conn.cursor() as cur:
        cur.execute(
            f"SELECT * FROM {table_name} where {condition}"
        )
        
        # a list of tuples
        result = cur.fetchall()
        return get_all_as_dict(result, fields)

def main():
    global headers, header_types, table
    headers = ['username','password','email','num']
    header_types = [STR_TYPE,STR_TYPE,STR_TYPE,INT_TYPE]
    table = 'Users'
    
    # create_table('Users', commit=False)
    
    # drop_table('Users')
    
    # upsert_one(
    #     {'username':'Steve2','password':"somepass","num":3},
    #     table_name='Users', fields=headers,commit=True
    # )
    
    # upsert_many(
    #     [{'username':'Steve','password':"somepass","num":3}, {'username':'Steve4','email':'j@hotmail.com', 'password':"somepass","num":2}],
    #     'Users', commit=True
    # )
    
    # delete_where("num = '2'", 'Users')
    
    # delete_where(get_condition("username", "Steve"), 'Users')
    
    # print(get_items())
    
    # print(get_items_where(get_condition('email',"d")))
    
    pass

'''
create a table
delete a whole table
- 
upsert one item
upsert multiple items
delete all items where (deleting one is not it in sql)
get all items
get all items where
-
all these methods work here.
'''
main()