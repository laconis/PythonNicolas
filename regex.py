pattern = re.compile(
    r'^TK_(?P<user>[^_]+)_'
    r'(?P<year>\d{4})_'
    r'(?P<month>\d{2})_'
    r'(?P<day>\d{2})_'
    r'(?P<hour>\d{2})_'
    r'(?P<minute>\d{2})_'
    r'(?P<second>\d{2})\.mp4$'
)

fichier = "TK_john_2026_04_10_23_00_00.mp4"
m = pattern.match(fichier)

if m:
    print("user :", m.group("user"))
    print("année :", m.group("year"))

CREATE TABLE videos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(100),
    datetime DATETIME,
    filename VARCHAR(255)
);

ALTER TABLE videos
ADD UNIQUE (filename);



 #Script reel 
import re
import mysql.connector
from datetime import datetime

pattern = re.compile(
    r'^TK_(?P<user>[^_]+)_'
    r'(?P<year>\d{4})_'
    r'(?P<month>\d{2})_'
    r'(?P<day>\d{2})_'
    r'(?P<hour>\d{2})_'
    r'(?P<minute>\d{2})_'
    r'(?P<second>\d{2})\.mp4$'
)

def enregistrer_video_mysql(filename):
    m = pattern.match(filename)
    if not m:
        print("Nom de fichier invalide :", filename)
        return

    data = m.groupdict()

    # Construire un datetime Python
    dt = datetime(
        int(data["year"]),
        int(data["month"]),
        int(data["day"]),
        int(data["hour"]),
        int(data["minute"]),
        int(data["second"])
    )

    # Connexion MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="motdepasse",
        database="ma_base"
    )
    cursor = conn.cursor()

    # Insertion
    cursor.execute(
        "INSERT INTO videos (user, datetime, filename) VALUES (%s, %s, %s)",
        (data["user"], dt, filename)
    )

    conn.commit()
    cursor.close()
    conn.close()

    print("Enregistré :", filename)

