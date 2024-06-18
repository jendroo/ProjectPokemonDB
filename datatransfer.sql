\COPY pokemon_data
FROM '/home/dci-student/DCIProjects/python_module/databases/ProjectPokemonDB/pokemon_data.csv'
DELIMITER ','
CSV HEADER;

\COPY pokemon_colors
FROM '/home/dci-student/DCIProjects/python_module/databases/ProjectPokemonDB/pokemon_colors.csv'
DELIMITER ','
CSV HEADER;

\COPY pokemon_shapes
FROM '/home/dci-student/DCIProjects/python_module/databases/ProjectPokemonDB/pokemon_shapes.csv'
DELIMITER ','
CSV HEADER;

\COPY types
FROM '/home/dci-student/DCIProjects/python_module/databases/ProjectPokemonDB/types.csv'
DELIMITER ','
CSV HEADER;

\COPY pokemon_types
FROM '/home/dci-student/DCIProjects/python_module/databases/ProjectPokemonDB/pokemon_types.csv'
DELIMITER ','
CSV HEADER;