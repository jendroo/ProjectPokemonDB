import argparse
import psycopg


def add_favorite(input_id):
    conn= psycopg.connect(
    dbname='pokemondb',
    user='postgres',
    password='postgres',
    host="localhost",
    port="5432"
    )

    cur = conn.cursor()

    query = """
    INSERT INTO favorites (pokemon_id) VALUES (%s);
    """
    cur.execute(query, (input_id,))
    conn.commit()
    print(f' Pokemon # {input_id} added to your favorites')

    cur.close()
    conn.close()

def favorites():
    
    conn= psycopg.connect(
    dbname='pokemondb',
    user='postgres',
    password='postgres',
    host="localhost",
    port="5432"
    )
    cur = conn.cursor()

    query = """SELECT f.pokemon_id, p.name
    FROM favorites as f
    INNER JOIN pokemon_data as p on f.pokemon_id = p.id;
    """
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(f'# {i[0]} - Name: {i[1].title()}')
        

    cur.close()
    conn.close()

def remove_favorite(input_id):
    
    conn= psycopg.connect(
    dbname='pokemondb',
    user='postgres',
    password='postgres',
    host="localhost",
    port="5432"
    )
    cur = conn.cursor()

    query = """
    DELETE FROM favorites pokemon_id WHERE pokemon_id = %s;
    """
    cur.execute(query, (input_id,))
    conn.commit()
    print(f' Pokemon # {input_id} removed from your favorites')

    cur.close()
    conn.close()

def info(input_id):
    conn= psycopg.connect(
    dbname='pokemondb',
    user='postgres',
    password='postgres',
    host="localhost",
    port="5432"
    )
    cur = conn.cursor()

    select_query = """ select id, name, array_agg(type) as types, color, shape from pokemon_overview  WHERE id = %s group by id, name, color, shape; """
    cur.execute(select_query, (input_id,))
    data = cur.fetchall()
    print(f'# {data[0][0]}'.title())
    print(f'Name: {data[0][1]}'.title())
    print(f'Type 1: {data[0][2][0]}'.title())
    try:
        print(f'Type 2: {data[0][2][1]}'.title())
    except IndexError:
        print('Type 2:  - ')
    print(f'Color: {data[0][3]}'.title())
    print(f'Shape: {data[0][4]}'.title())

    cur.close()
    conn.close()

def pokedex():
    conn= psycopg.connect(
    dbname='pokemondb',
    user='postgres',
    password='postgres',
    host="localhost",
    port="5432"
    )
    cur = conn.cursor()

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

if __name__ == "__main__":
    parser =  argparse.ArgumentParser(description='Pokemon DB')
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-p", "--pokedex", help="Shows entire pokedex(gen1)", action='store_true')
    group.add_argument("-f", "--favorites", help="shows your favorite list", action='store_true')
    parser.add_argument("-a", "--add",type=int, metavar='pokemon_id', help="adds pokemon to favorite list via id", choices=range(1, 152))
    parser.add_argument("-r", "--remove",type=int, metavar='pokemon_id', help="removes pokemon from favorite list via id", choices=range(1, 152))
    parser.add_argument("-i", "--info", metavar="pokemon id", type= int, help="show info of the pokemon with given id",choices=range(1, 152))
    arguments = parser.parse_args()

    if arguments.pokedex:
        pokedex()
    if arguments.favorites:
        favorites()
    if arguments.add:
        add_favorite(arguments.add)
    if arguments.remove:
        remove_favorite(arguments.remove)
    if arguments.info:
        try:
            info(arguments.info)
        except IndexError:
            print("Please enter a valid id between 1 and 151!")




