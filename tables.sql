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

CREATE or replace view pokemon_overview as
    select p.id, p.name, t.name as type, c.color as color, s.shape as shape, p.height as height, p.weight as weight
    from pokemon_data as p
    inner join pokemon_types as pt on p.id = pt.pokemon_id
    inner join types as t on pt.type_id = t.id
    inner join pokemon_colors as c on p.color_id = c.id
    inner join pokemon_shapes as s on p.shape_id = s.id;
