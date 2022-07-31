# run on terminal
'''
cockroach sql --url "postgresql://brayton:51gSHp3yJ9LrRY7ox0lbTw@free-tier6.gcp-asia-southeast1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dpurer-oriole-3004&sslmode=verify-full&
sslrootcert=%2F$HOME%2F.postgresql%2Froot.crt"

no space
'''
import psycopg2

conn = psycopg2.connect("postgresql://brayton:51gSHp3yJ9LrRY7ox0lbTw@free-tier6.gcp-asia-southeast1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dpurer-oriole-3004")

STR_TYPE = 'VARCHAR(60)'
LINK_TYPE = 'VARCHAR(600)'

def create_one_table():
    with conn.cursor() as cur:
        cur.execute(
            f'create table if not exists testdata (sometext {STR_TYPE}, somenum INT )'
        )
        
        # cur.execute(
        #      "CREATE TABLE IF NOT EXISTS search_table (img_url VARCHAR(600), name VARCHAR(60), extern_link VARCHAR(600), price INT, product_img_link VARCHAR(600) )"
        # )       
    
    conn.commit()  
    
def insert_one(text, num):
    with conn.cursor() as cur: 
        cur.execute(
            f"upsert into testdata (sometext, somenum) values ('{text}', '{num}')"
        )
        
    conn.commit()
    
def remove_where(condition):
    with conn.cursor() as cur: 
        cur.execute(
            f"delete from testdata where {condition}"
        )
        
    conn.commit()
    
def get_all():
    with conn.cursor() as cur:
        cur.execute(
            f"SELECT * FROM testdata"
        )
        
        # a list of tuples
        result = cur.fetchall()
        return result

def get_all_as_dict():
    headers = ['sometext', 'somenum']
    res = get_all()
    arr = []
    for each in res:
        doc = {}
        for i in range(len(headers)):
            header = headers[i]
            doc[header] = each[i]
        arr.append(doc)
    return arr

# create_one_table()
# insert_one("hello world", 34)
# insert_one("hello world 2", 35)
# insert_one("hello world 3", 36)
# remove_where("somenum = '34'")