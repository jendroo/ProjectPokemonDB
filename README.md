# A Pokedex Command Line Application

## learning project
### mvp - shows base functionality. Infinite room for improvements
The topic of this database was chosen because of my passion for pokemon as a child. Originally I started to create a book database,
but since it was covered in the course as example, I wanted to do something else. This database is limited to the first generation of pokemon, because that's all I know.

### Goals
- Combine the lessons of python, argparse and sql
- Show CRUD actions on DB
- functionality via terminal

## Mission Statement:
Have a well organized pokemon database, that quickly let's you access all wanted information.

## Mission Objectives
- Have data of all generation 1 pokemon
- Show detailed individual information
- Show "Pokedex"
- Create favorite lists
- And hopefully more to come

## How to use

### Prequsites
- [postgresql](https://www.postgresql.org/)
- [psycopg](https://www.psycopg.org/)

Initiate the database
- Open a postgres terminal in the project directory
- First run `\i sql/tables.sql`
- Then run `\i sql/datatransfer.sql`
- In a bash terminal from the directory run `python3 src/main.py -h` for further instructions
- And of course you can run any queries you want on top to the built-in options


## About

### Challenges
- lessons on different elements were taught in a vacuum
- connecting everything correctly
- pass arguments and parameters correctly

### Features
- Have a full pokedex available in your terminal (only based on G1):
    - View whole pokedex
    - Show individual pokemon information
    - Add pokemon to a favorite list
    - Remove pokemon from favorite list
    - Show favorite list

### Things I couldn't implement because of time (yet)
- Create your team of 6 pokemon like in the game
- Have the possibility of multiple users with
    - Individual favorite lists
    - Individual team lists


### What I need to look into
- I have to look into `make`, which apparently allows you to setup your database automatically
- structuring


### What I learned
- Views: weren't really covered in class. Create virtual tables
- A well established database can be the foundation for your application
    - E.G.: While working on the pokemon database I realised that a big portion of the original game was just a big database
- If understood correctly, it is preferred to create and close a new connection for each query. It improves performance and prevents SQL injection
- I truly know nothing about performance yet