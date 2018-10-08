DROP TABLE IF EXISTS tbuczniowie;
CREATE TABLE tbuczniowie
(
  id_ucznia INTEGER PRIMARY KEY NOT NULL,
  nazwisko TEXT (20),
  imie TEXT (20),
  ulica TEXT(30),
  dom INTEGER,
  id_klasy INTEGER
);

DROP TABLE IF EXISTS tboceny;
CREATE TABLE tboceny
(
    id_ucznia INTEGER NOT NULL,
	ocena INTEGER,
    data DATE,
    id_przedmiotu INTEGER,
  FOREIGN KEY(id_ucznia) REFERENCES tbuczniowie(id_ucznia)


);
DROP TABLE IF EXISTS tbprzedmioty;
CREATE TABLE tbprzedmioty
(
  id_przedmiotu INTEGER NOT NULL,
  nazwa_przedmiotu TEXT (20),
  nazwisko_nauczyciela TEXT (30),
  imie_nauczyciela TEXT (15),
  FOREIGN KEY(id_przedmiotu) REFERENCES tboceny(id_przedmiotu)
);
