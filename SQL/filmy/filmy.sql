DROP TABLE IF EXISTS filmy;
CREATE TABLE filmy (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    genere TEXT DEFAULT  '',
    year INTEGER,
    rating DECIMAL
);
