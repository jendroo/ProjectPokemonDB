\COPY pokemon_data
FROM 'data/pokemon_data.csv'
DELIMITER ','
CSV HEADER;

\COPY pokemon_colors
FROM 'data/pokemon_colors.csv'
DELIMITER ','
CSV HEADER;

\COPY pokemon_shapes
FROM 'data/pokemon_shapes.csv'
DELIMITER ','
CSV HEADER;

\COPY types
FROM 'data/types.csv'
DELIMITER ','
CSV HEADER;

\COPY pokemon_types
FROM 'data/pokemon_types.csv'
DELIMITER ','
CSV HEADER;