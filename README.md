# A Pokedex Command Line Application

## learning project
### mvp - shows base functionality. Infinite room for improvements

### Goals
- Combine the lessons of python, argparse and sql
- Show CRUD actions on DB
- functionality via terminal

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