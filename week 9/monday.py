import sqlite3
import csv
import pathlib

with open('corrected_pokemon_names.csv', 'r',
          encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)
## check the data
# print(headers)
# print(data[:10])

db_target = pathlib.Path('pokemon.db')
if db_target.exists():
    db_target.unlink()

conn = sqlite3.connect(db_target)

c = conn.cursor()

c.execute("CREATE TABLE pokemon "
          "(dex text, eng_name text, "
          "description text);")

stuff = c.executemany("INSERT INTO pokemon "
              "VALUES (?, ?, ?)", data)

conn.commit()

