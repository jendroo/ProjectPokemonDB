CREATE or replace view pokemon_overview as
    select p.id, p.name, t.name as type, c.color as color, s.shape as shape, p.height as height, p.weight as weight
    from pokemon_data as p
    inner join pokemon_types as pt on p.id = pt.pokemon_id
    inner join types as t on pt.type_id = t.id
    inner join pokemon_colors as c on p.color_id = c.id
    inner join pokemon_shapes as s on p.shape_id = s.id;

-- Pokedex Query
select id, name, array_agg(type) as types, color, shape, height, weight from pokemon_overview group by id, name, color, shape, height, weight;

-- Pokeinfo Query
select id, name, array_agg(type) as types, color, shape from pokemon_overview WHERE id = %s group by id, name, color, shape;


-- Query to show favorites
SELECT f.pokemon_id, p.name
FROM favorites as f
INNER JOIN pokemon_data as p on f.pokemon_id = p.id;