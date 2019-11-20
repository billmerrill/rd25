import csv
import sqlite3

SSME_DB = "db/ssme.db"

engine_flights = []
with open("data/ssme-flight-map.csv") as efh:
    reader = csv.DictReader(efh)
    for row in reader:
        engine_flights.append(dict(row))

flights = {x["flight"] for x in engine_flights}
engines = {(x["engine"], x["powerhead"]) for x in engine_flights}

connection = sqlite3.connect(SSME_DB)
with connection:
    for fl in flights:
        connection.execute("INSERT INTO flight (ksc_number) VALUES (?)", (str(fl),))
    for en in engines:
        connection.execute(
            "INSERT INTO engine (engine_number, powerhead_number) VALUES (?,?)",
            (str(en[0]), str(en[1])),
        )
    for enfl in engine_flights:
        sql = """
        INSERT INTO engine_flight (engine_id, flight_id)
        SELECT sa.id, sb.id FROM
        (SELECT id from engine where engine_number = ? and powerhead_number=?) sa,
        (SELECT id from flight where ksc_number = ?) sb
        """
        connection.execute(sql, (enfl["engine"], enfl["powerhead"], enfl["flight"]))
