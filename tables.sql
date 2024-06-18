CREATE DATABASE pokemondb;

\c pokemondb

CREATE TABLE IF NOT EXISTS pokemon_data (
    id SERIAL PRIMARY KEY, 
    name varchar(100) not null,
    height int not null,
    weight int not null,
    base_experience int not null,
    evolves_from_species_id int,
    evolution_chain_id int,
    color_id int not null,
    shape_id int not null,
    capture_rate int not null,
    is_legendary BOOLEAN
);

create table if not exists pokemon_shapes (
    id serial,
    shape varchar(100)
);

create table if not exists pokemon_colors (
    id serial,
    color varchar(100)
);

create table if not exists types (
    id SERIAL PRIMARY KEY,
    name varchar(100) not null
);

create table if not exists pokemon_types (
    pokemon_id int REFERENCES pokemon_data(id),
    type_id int not null REFERENCES types(id),
    slot int not null
);

create table if not exists favorites (
    fav_id SERIAL PRIMARY KEY,
    pokemon_id int REFERENCES pokemon_data(id)
);


