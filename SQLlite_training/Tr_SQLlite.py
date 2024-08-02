import sqlite3
from pathlib import Path
import os
from datetime import datetime

sql_file = os.path.join(Path(__file__).resolve().parent, 'app.db')

connect = sqlite3.connect(sql_file)

cr = connect.cursor()

cr.execute("""CREATE TABLE IF NOT exists User (
            id integer unique primary key autoincrement,
            username varchar(120) UNIQUE NOT NULL,
            email varchar(200) UNIQUE NOT NULL,
            joined_at DATE
           )
           """)

cr.execute("""CREATE TABLE IF NOT exists Profile (
            id integer unique primary key autoincrement,
            user integer unique,
            avatar BLOB,
            name varchar(200),
            bio TEXT,
            FOREIGN KEY (user) REFERENCES User(id)
           )
           """)

current_date = datetime.now().date().strftime('%Y-%m-%d')



# cr.execute(f"""INSERT INTO User (username, email, joined_at)
#            VALUES ("dexter", "dexter@aol.com", ?)
#            """, (current_date,))


def image_to_hex(image_path):
    with open(image_path, 'rb') as f:
        image_binary = f.read()
    return "x'" + image_binary.hex().upper() + "'"

avatar_path = os.path.join(Path(__file__).resolve().parent, 'dexter.png')
hex_avatar = image_to_hex(avatar_path)

user_id, name, bio = 1, "Dexter", "Hello, I am Dexter from the US"

# cr.execute("""INSERT INTO Profile (user, avatar, name, bio)
#               VALUES (?, ?, ?, ?)""",
#            (user_id, hex_avatar, name, bio))

connect.commit()

cr.execute("SELECT * FROM Profile")

rows = cr.fetchall()

cr.close()
connect.close()

