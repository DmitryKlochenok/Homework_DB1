import sqlite3
import json

def title_search(title):
    with  sqlite3.connect("netflix.db") as connection:
        cur = connection.cursor()
        cur.execute(f"""
    SELECT *
    FROM netflix
    WHERE title='{title}'
    ORDER BY date_added DESC
    LIMIT 1""")

        found = cur.fetchone()

        result = {
        "title": found[2],
        "country": found[5],
        "release_year": found[7],
        "genre": found[11],
        "description": found[12]
    }
        return result


def range_search(year_from, year_to):
    with sqlite3.connect("netflix.db") as connection:
        cur = connection.cursor()
        cur.execute(f"""
    SELECT title, release_year
    FROM netflix
    WHERE release_year BETWEEN {year_from} AND {year_to}
    LIMIT 100""")

        result = []
        found = cur.fetchall()

        for item in found:
            result.append({"title": item[0],
                           "release_year": item[1]})

    return result

def rating_search(rating):
    if rating == "children":
        with sqlite3.connect("netflix.db") as connection:
            cur = connection.cursor()
            cur.execute(f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating='G'""")

            found = cur.fetchall()

    if rating == "family":
        with sqlite3.connect("netflix.db") as connection:
            cur = connection.cursor()
            cur.execute(f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating='G' OR 'PG' OR 'PG-13'""")

            found = cur.fetchall()

    if rating == "adult":
        with sqlite3.connect("netflix.db") as connection:
            cur = connection.cursor()
            cur.execute(f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating='R' OR 'NC-17'""")

            found = cur.fetchall()

    result = []
    for item in found:
        result.append({
	 "title":item[0],
	 "rating": item[1],
	 "description":item[2]
	})


    return result


def genre_search(genre):
    with sqlite3.connect("netflix.db") as connection:
        cur = connection.cursor()
        cur.execute(f"""
               SELECT title, description
               FROM netflix
               WHERE listed_in LIKE '%{genre}%'
               ORDER BY date_added DESC
               LIMIT 10
""")
        result = []
        found = cur.fetchall()

        for item in found:
            result.append({"title": item[0],
                           "description": item[1]})

    return result


def pair_search(name1, name2):
    with sqlite3.connect("netflix.db") as connection:
        cur = connection.cursor()
        cur.execute(f"""
                   SELECT cast
                   FROM netflix
                   WHERE cast LIKE '%{name1}%' AND '%{name2}%' """)

        found = cur.fetchall()

    return found

def type_search(type, year, genre):
    with sqlite3.connect("netflix.db") as connection:
        cur = connection.cursor()
        cur.execute(f"""
                      SELECT title, description
                      FROM netflix
                      WHERE type='{type}' AND release_year='{year}', AND listed_in LIKE '%{genre}%' """)

        found = cur.fetchall()

    return found
