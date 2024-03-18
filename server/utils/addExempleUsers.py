import mysql.connector

def addExempleUsers(cursor, db):
    try:
        cursor.execute("""
            INSERT INTO users (nom, prenom, email, password, admin)
            VALUES (%s, %s, %s, %s, %s)
        """, ('Admin', 'Admin', 'admin@example.com', 'password123', True))

        cursor.execute("""
            INSERT INTO users (nom, prenom, email, password, admin)
            VALUES (%s, %s, %s, %s, %s)
        """, ('Utilisateur', 'Normal', 'user@example.com', 'password456', False))

        print("Deux utilisateurs ont été ajoutés à la table 'users'.")

        # Valider et effectuer les changements dans la base de données
        db.commit()

    except mysql.connector.Error as error:
        print(f"Error: {error}")
