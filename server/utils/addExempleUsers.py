import mysql.connector

def addExempleUsers(cursor, db):
    try:
        # Check if the name 'Admin' already exists in the table
        cursor.execute("SELECT * FROM users WHERE nom = 'Admin'")
        admin_exists = cursor.fetchone()

        if not admin_exists:
            # If 'Admin' doesn't exist, insert it into the table
            cursor.execute("""
                INSERT INTO users (nom, prenom, email, password, admin)
                VALUES (%s, %s, %s, %s, %s)
            """, ('Admin', 'Admin', 'admin@example.com', 'password123', True))
            print("Utilisateur 'Admin' a été ajouté à la table 'users'.")
        else:
            print("L'utilisateur 'Admin' existe déjà.")

        # Check if the name 'Utilisateur' already exists in the table
        cursor.execute("SELECT * FROM users WHERE nom = 'Utilisateur'")
        user_exists = cursor.fetchone()

        if not user_exists:
            # If 'Utilisateur' doesn't exist, insert it into the table
            cursor.execute("""
                INSERT INTO users (nom, prenom, email, password, admin)
                VALUES (%s, %s, %s, %s, %s)
            """, ('Utilisateur', 'Normal', 'user@example.com', 'password456', False))
            print("Utilisateur 'Utilisateur' a été ajouté à la table 'users'.")
        else:
            print("L'utilisateur 'Utilisateur' existe déjà.")

        # Commit the changes to the database
        db.commit()

    except mysql.connector.Error as error:
        # Rollback the transaction if an error occurs
        db.rollback()
        print(f"Error: {error}")
