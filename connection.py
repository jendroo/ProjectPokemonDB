import psycopg

## DB connection

conn= psycopg.connect(
    dbname='pokemondb',
    user='postgres',
    password='postgres',
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# View pokemon
# input_id = int(input('Please enter a pokemon id: '))

# select_query = """ select id, name, array_agg(type) as types, color, shape from pokemon_overview  WHERE id = %s group by id, name, color, shape; """
# cur.execute(select_query, (input_id,))
# data = cur.fetchall()
# print(f'# {data[0][0]}'.title())
# print(f'Name: {data[0][1]}'.title())
# print(f'Type 1: {data[0][2][0]}'.title())
# try:
#     print(f'Type 2: {data[0][2][1]}'.title())
# except IndexError:
#     print('Type 2:  - ')
# print(f'Color: {data[0][3]}'.title())
# print(f'Shape: {data[0][4]}'.title())


query = """
    select id, name, array_agg(type) as types, color, shape, height, weight from pokemon_overview
    group by id, name, color, shape, height, weight;
    """

cur.execute(query)
data = cur.fetchall()
for i in data:
    print(f'# {i[0]} - Name: {i[1].title()} -- Types:{i[2]} -- Color: {i[3].title()} --- Shape: {i[4].title()} --- Height: {i[5]}" --- Weight: {i[6]} lbs')





cur.close()
conn.close()

