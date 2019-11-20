-- DROP TABLE engine;
CREATE TABLE engine (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  engine_number TEXT,
  powerhead_number TEXT
);

-- DROP TABLE flight;
CREATE TABLE flight (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ksc_number TEXT
);

-- DROP TABLE engine_flight;
CREATE TABLE engine_flight (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  engine_id INTEGER,
  flight_id INTEGER
);
