from mysql.connector import connection

cnx = connection.MySQLConnection(user='root', password='mysql',
                                 host='127.0.0.1',
                                 database='kiralyok')
cursor = cnx.cursor()

# Táblák mutatása
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
print()

# Uralkodó tábla adatainak lekérdezése
cursor.execute("SELECT * FROM uralkodo")
for uralkodo in cursor:
    print(uralkodo)
print()

# 2. feladat
print("2. feladat")
cursor.execute("SELECT nev, ragnev FROM uralkodo WHERE ragnev != '' ORDER BY szul;")
for uralkodo in cursor:
    print(uralkodo) 
print()

# 3. feladat
print("3. feladat")
cursor.execute("""
    SELECT uralkodo.nev, hivatal.mettol, hivatal.meddig
    FROM uralkodo
    JOIN hivatal ON uralkodo.azon = hivatal.uralkodo_az
    JOIN uralkodohaz ON uralkodo.uhaz_az = uralkodohaz.azon
    WHERE uralkodohaz.nev = 'Árpád-ház'
    ORDER BY hivatal.mettol;
""")
for uralkodo in cursor:
    print(uralkodo)
print()

# 4. feladat
print("4. feladat")
cursor.execute("""
    SELECT uralkodo.nev 
    FROM uralkodo 
    JOIN hivatal ON uralkodo.azon = hivatal.uralkodo_az 
    WHERE hivatal.koronazas > hivatal.mettol
""")
for uralkodo in cursor:
    print(uralkodo)
print()

# 5. feladat 
print("5. feladat")
cursor.execute("""
    SELECT uralkodo.nev 
    FROM uralkodo 
    JOIN hivatal ON uralkodo.azon = hivatal.uralkodo_az 
    WHERE hivatal.mettol BETWEEN 1601 AND 1700 
      AND hivatal.meddig BETWEEN 1601 AND 1700
""")
for uralkodo in cursor:
    print(uralkodo)
print()

# 6. feladat
print("6. feladat")
cursor.execute("""
    SELECT uralkodo.nev, (hivatal.meddig - hivatal.mettol) AS uralkodasi_ido 
    FROM hivatal 
    JOIN uralkodo ON hivatal.uralkodo_az = uralkodo.azon 
    ORDER BY uralkodasi_ido DESC 
    LIMIT 1
""")
for uralkodo in cursor:
    print(uralkodo)
print()

# 7. feladat
print("7. feladat")
cursor.execute("""
    SELECT uralkodo.nev, (hivatal.mettol - uralkodo.szul) 
    FROM uralkodo 
    JOIN hivatal ON uralkodo.azon = hivatal.uralkodo_az 
    JOIN uralkodohaz ON uralkodo.uhaz_az = uralkodohaz.azon 
    WHERE (hivatal.mettol - uralkodo.szul) < 15 
    ORDER BY (hivatal.mettol - uralkodo.szul) ASC
""")
for uralkodo in cursor:
    print(uralkodo)
print()

# 8. feladat
print("8. feladat")
cursor.execute("""
    SELECT uralkodo.nev, SUM(hivatal.meddig - hivatal.mettol) AS osszes_uralkodasi_ido 
    FROM hivatal 
    JOIN uralkodo ON hivatal.uralkodo_az = uralkodo.azon 
    GROUP BY uralkodo.nev 
    HAVING COUNT(hivatal.azon) > 1 
    ORDER BY osszes_uralkodasi_ido DESC
""")
for uralkodo in cursor:
    print(uralkodo)
print()

# 9. feladat
print("9. feladat")
cursor.execute("""
    SELECT uralkodohaz.nev AS uralkodohaz_nev, 
           COUNT(DISTINCT uralkodo.azon) AS uralkodok_szama 
    FROM uralkodo 
    JOIN uralkodohaz ON uralkodo.uhaz_az = uralkodohaz.azon 
    GROUP BY uralkodohaz.nev 
    ORDER BY uralkodok_szama DESC
""")
for uralkodo in cursor:
    print(uralkodo)
print()

cursor.close()
cnx.close()