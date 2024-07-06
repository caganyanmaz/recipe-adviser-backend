
BEGIN;

CREATE TABLE IF NOT EXISTS recipe (
	id INTEGER PRIMARY KEY,
	title TEXT,
	time INTEGER,
	url TEXT,
	photourl TEXT
);

CREATE TABLE IF NOT EXISTS tag (
	id INTEGER PRIMARY KEY,
	name TEXT
);

CREATE TABLE IF NOT EXISTS ingredient_recipe (
	recipe_id INTEGER,
	description TEXT,
	FOREIGN KEY (recipe_id) REFERENCES recipe (id)
);

CREATE TABLE IF NOT EXISTS tag_recipe (
	tag_id INTEGER,
	recipe_id INTEGER,
	FOREIGN KEY (tag_id) REFERENCES tag (id),
	FOREIGN KEY (recipe_id) REFERENCES recipe (id)
);

CREATE TABLE IF NOT EXISTS instruction_recipe (
	recipe_id INTEGER,
	ord INTEGER,
	description TEXT,
	FOREIGN KEY(recipe_id) REFERENCES recipe(id)
);

CREATE INDEX IF NOT EXISTS recipe_id_idx ON recipe (id);
CREATE INDEX IF NOT EXISTS ingredient_recipe_id_idx ON ingredient_recipe (recipe_id);
CREATE INDEX IF NOT EXISTS instruction_recipe_id_idx ON instruction_recipe (recipe_id);

COMMIT;
