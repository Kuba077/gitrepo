DROP TABLE IF EXISTS uczniowie;

CREATE TABLE uczniowie(
id INTEGER PRIMARY KEY NOT NULL, 
imie TEXT,
nazwisko TEXT,
plec BOOLEAN,
id_klasa INTEGER NOT NULL,
egz_hum NUMERIC NOT NULL DEFAULT 0,
egz_mat NUMERIC NOT NULL DEFAULT 0,
egz_jez NUMERIC NOT NULL DEFAULT 0,
FOREIGN KEY (id_klasa) REFERENCES klasy (id)

);

DROP TABLE IF EXISTS klasy;

CREATE TABLE klasy(
id INTEGER NOT NULL,
klasa TEXT,
rok_naboru INTEGER,
rok_matury INTEGER
);

DROP TABLE IF EXISTS przedmioty;

CREATE TABLE przedmioty(
id INTEGER NOT NULL,
przedmiot TEXT(20),
imie_naucz TEXT(15),
nazwisko_naucz TEXT(20),
plec_naucz BOOLEAN
);

DROP TABLE IF EXISTS oceny;

CREATE TABLE oceny(
id INTEGER NOT NULL,
datad DATE,
id_uczen INTEGER NOT NULL,
id_przedmiot INTEGER NOT NULL,
ocena DECIMAL,
FOREIGN KEY (id_uczen) REFERENCES uczniowie(id),
FOREIGN KEY (id_przedmiot) REFERENCES przedmioty(id)
 
);
