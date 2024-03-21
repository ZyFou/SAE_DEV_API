import mysql.connector

def addExempleUsers(db_infos):
    try:
        db = mysql.connector.connect(
            host=db_infos['host'],
            user=db_infos['user'],
            password=db_infos['password'],
            database=db_infos['database']
        )
        cursor = db.cursor()

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
                INSERT INTO users (nom, prenom, email, password, admin, experience, level)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, ('Utilisateur', 'Normal', 'user@example.com', 'password456', False,0,1))
            print("Utilisateur 'Utilisateur' a été ajouté à la table 'users'.")
        else:
            print("L'utilisateur 'Utilisateur' existe déjà.")

        # Commit the changes to the database
        db.commit()

        cursor.close()
        db.close()

    except mysql.connector.Error as error:
        # Rollback the transaction if an error occurs
        db.rollback()
        print(f"Error: {error}")
        cursor.close()
        db.close()


def addCharacters(db_infos):
    try:
        db = mysql.connector.connect(
            host=db_infos['host'],
            user=db_infos['user'],
            password=db_infos['password'],
            database=db_infos['database']
        )
        cursor = db.cursor()

        # Vérifier si les personnages existent déjà dans la table
        cursor.execute("SELECT COUNT(*) FROM characters")
        characters_count = cursor.fetchone()[0]

        if characters_count == 0: 
            goku_image = "https://dragonball-legends.com/assets/characters/0278_kakarot_278_texture/Texture2D/0278_Kakarot_278_Chara.png"
            cursor.execute("""
                INSERT INTO characters (name, race, image, description, strength, defense, speed, health, energy)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Goku', 'Saiyan', goku_image, 'Grand guerrier Saiyan ayant grandi sur Terre.', 90, 80, 65, 1800, 800))
            print("Personnage 'Goku' ajouté à la table 'characters'.")


            vegeta_image = "https://dragonball-legends.com/assets/characters/0257_vegeta_257_texture/Texture2D/0257_Vegeta_257_Effect06.png"
            cursor.execute("""
                INSERT INTO characters (name, race, image, description, strength, defense, speed, health, energy)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Vegeta', 'Saiyan', vegeta_image, 'Fier prince des Saiyans.', 85, 85, 60, 1750, 800))
            print("Personnage 'Vegeta' ajouté à la table 'characters'.")

            tao_pai_pai_image = "https://dragonball-legends.com/assets/characters/0309_taopaipai_309_texture/Texture2D/0309_TaoPaiPai_309_Effect3.png"
            cursor.execute("""
                INSERT INTO characters (name, race, image, description, strength, defense, speed, health, energy)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, ('TaoPaiPai', 'Human',tao_pai_pai_image, 'Tristement connu assassin à renommée mondiale capable de tuer avec sa langue.', 40, 50, 80, 1300, 600))
            print("Personnage 'TaoPaiPai' ajouté à la table 'characters'.")

            db.commit()
        else:
            print("Les personnages existent déjà dans la table 'characters'.")

        cursor.close()
        db.close()

    except mysql.connector.Error as error:
        db.rollback()
        print(f"Erreur: {error}")
        cursor.close()
        db.close()


def addTechniques(db_infos):
    try:
        db = mysql.connector.connect(
            host=db_infos['host'],
            user=db_infos['user'],
            password=db_infos['password'],
            database=db_infos['database']
        )
        cursor = db.cursor()

        # Vérifier si les personnages existent déjà dans la table
        cursor.execute("SELECT COUNT(*) FROM techniques")
        techniques_count = cursor.fetchone()[0]

        if techniques_count == 0:  # Si la table est vide, ajouter les personnages
            # Ajout du premier personnage
            cursor.execute("""
                INSERT INTO techniques (name, description, type, damages, accuracy, cost, cooldown)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, ('kamehameha', "Technique emblématique de l'univers de dragon ball", "kikoha",120,65,40,0))
            print("Technique 'kamehameha' ajouté à la table 'techniques'.")

            
            db.commit()
        else:
            print("Les techniques existent déjà dans la table 'techniques'.")

        cursor.close()
        db.close()

    except mysql.connector.Error as error:
        db.rollback()
        print(f"Erreur: {error}")
        cursor.close()
        db.close()
