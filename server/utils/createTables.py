import mysql.connector

def createUserTable(cursor):
    cursor.execute("SHOW TABLES LIKE 'users'")
    result = cursor.fetchone()

    if not result:
        cursor.execute("""
                CREATE TABLE users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nickname VARCHAR(255),
                    nom VARCHAR(255),
                    prenom VARCHAR(255),
                    email VARCHAR(255),
                    password VARCHAR(255),
                    admin BOOLEAN,
                    profile_picture VARCHAR(255),
                    banner VARCHAR(255),
                    favorite_character VARCHAR(255),
                    collection_id INT
                )
            """)
        print("La table 'users' a été créée avec succès.")
    else:
        print("La table 'users' existe déjà.")
