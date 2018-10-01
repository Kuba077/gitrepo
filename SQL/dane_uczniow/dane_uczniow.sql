DROP TABLE IF EXISTS tbnazwiska;
CREATE TABLE tbnazwiska
(
  nr_ucznia INTEGER PRIMARY KEY NOT NULL,
  nazwisko TEXT,
  imie1 TEXT,
  imie2 TEXT
);

DROP TABLE IF EXISTS tbdane;
CREATE TABLE tbdane
(
	nr_ucznia INTEGER NOT NULL,
	dzien INTEGER,
  miesiac INTEGER,
  rok INTEGER,
  m_urodzenia TEXT,
  wojewodztwo TEXT,
  FOREIGN KEY(nr_ucznia) REFERENCES tbnazwiska(nr_ucznia)


);
DROP TABLE IF EXISTS tboceny;
CREATE TABLE tboceny
(
  nr_ucznia INTEGER NOT NULL,
  zachowanie TEXT,
  religia INTEGER,
  rel INTEGER,
  ety INTEGER,
  jpol INTEGER,
  jang INTEGER,
  jniem INTEGER,
  mat INTEGER,
  his INTEGER,
  geog INTEGER,
  biol INTEGER,
  fiz INTEGER,
  che INTEGER,
  tech INTEGER,
  info INTEGER,
  plas INTEGER,
  po INTEGER,
  wf INTEGER,
  FOREIGN KEY(nr_ucznia) REFERENCES tbnazwiska(nr_ucznia)
);
