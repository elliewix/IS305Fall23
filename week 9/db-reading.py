import sqlite3

conn = sqlite3.connect('pokemon.db')

c = conn.cursor()``

result = c.execute("SELECT * FROM pokemon;")
print(type(result))

# print(result.fetchone())
# print(result.fetchmany(10))
all_content = result.fetchall()
print(type(all_content))

print(len(all_content))