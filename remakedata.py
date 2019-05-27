import pandas as pd
import sqlite3
import glob
from text_preprocessing import *
from SQLiteHelper import *

text_prep = Preprocessing('vietnamese-stopwords.txt')

def convert_data_to_database():
    data_db= SQLiteHelper('resource/data.db')
    data_db.create_table("""CREATE TABLE data(
            link TEXT NOT NULL,
            title TEXT NOT NULL,
            location TEXT NOT NULL,
            image TEXT NOT NULL,
            area TEXT NOT NULL,
            price TEXT NOT NULL
        )
        """)
    data = pd.read_csv('resource/data.csv', sep = ' ', chunksize = 1000)
    for detail_chunk in data:
        for _, row in detail_chunk.iterrows():
            row = list(map(lambda x: str(x).replace("\"", "'"), row))
            data_db.edit("INSERT INTO data (link, title, location, image, area, price) VALUES(\"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")"%(row[0], row[1], row[2], row[3], row[4], row[5]))

            
convert_data_to_database()