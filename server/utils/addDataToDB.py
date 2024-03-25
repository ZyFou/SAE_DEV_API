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
                INSERT INTO users (nom, prenom, email, password, admin,profile_picture, experience, level)
                VALUES (%s, %s, %s, %s, %s, %s, %s,%s)
            """, ('Utilisateur', 'Normal', 'user@example.com', 'password456', False, "https://i.pinimg.com/564x/b1/79/47/b17947cd9653a08b2801d11afd291d2d.jpg",0,1))
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

            gohan_image = "https://dragonball-legends.com/assets/characters/0258_gohanfuture_258_texture/Texture2D/0258_GohanFuture_258_Chara.png"
            cursor.execute("""
                INSERT INTO characters (name, race, image, description, strength, defense, speed, health, energy)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Gohan', 'Saiyan',gohan_image, 'Fils de Goku et saiyan hybride au potentiel infini.', 75, 75, 60, 1600, 900))
            print("Personnage 'Gohan' ajouté à la table 'characters'.")

            piccolo_image = "https://dragonball-legends.com/assets/characters/0445_piccolohl_445_texture/Texture2D/0445_PiccoloHL_445_Chara.png"
            cursor.execute("""
                INSERT INTO characters (name, race, image, description, strength, defense, speed, health, energy)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Piccolo', 'Namek',piccolo_image, 'Grand namek fort.', 60, 80, 55, 2000, 800))
            print("Personnage 'Gohan' ajouté à la table 'characters'.")


            goku_ssj1_image = "https://dragonball-legends.com/assets/characters/0563_gokuss1_563_texture/Texture2D/0563_GokuSS1_563_Chara_00.png"
            cursor.execute("""
                INSERT INTO characters (name, race, image, description, strength, defense, speed, health, energy)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Super Saiyan Goku', 'Saiyan', goku_ssj1_image, 'Première apparition d"un super Saiyan dans la série.', 95, 70, 70, 1500, 650))
            print("Personnage ' ssj1' ajouté à la table 'characters'.")

            vegeta_ssj1_image = "https://dragonball-legends.com/assets/characters/0257_vegeta_257_texture/Texture2D/0257_Vegeta_257_Effect15.png"
            cursor.execute("""
                INSERT INTO characters (name, race, image, description, strength, defense, speed, health, energy)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Super Saiyan Vegeta', 'Saiyan', vegeta_ssj1_image, 'Éveil du prince des saiyans au stade de super saiyan !', 90, 85, 70, 1800, 650))
            print("Personnage 'Vegeta ssj1' ajouté à la table 'characters'.")


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

            normal_attack_gif = "https://c.tenor.com/ApaFfLf7DzsAAAAC/tenor.gif"
            cursor.execute("""
                INSERT INTO techniques (name, description, image, type, damages, accuracy, cost, cooldown)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, ('NormalAttack', "Enchainnement de coups simple mais effiace.", normal_attack_gif, "normal_attack",50,50,20,0))
            print("Technique 'Normal Attack' ajouté à la table 'techniques'.")

            guard_gif = "https://c.tenor.com/0MAPePoGxQ4AAAAC/tenor.gif"
            cursor.execute("""
                INSERT INTO techniques (name, description, image, type, damages, accuracy, cost, cooldown)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Guard', "Technique defensive visant uniquement à bloquer une attaque.", guard_gif, "block_attack",0,40,50,1))
            print("Technique 'Guard' ajouté à la table 'techniques'.")

            counter_gif = "https://c.tenor.com/pbJ9Nuz-0y0AAAAC/tenor.gif"
            cursor.execute("""
                INSERT INTO techniques (name, description, image, type, damages, accuracy, cost, cooldown)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Counter', "Attaque de contre qui à un gros risque d'échouer mais peut être très efficace.", counter_gif, "counter_attack",150,20,50,2))
            print("Technique 'Counter' ajouté à la table 'techniques'.")


            kamehameha_gif = "https://c.tenor.com/DcU1rwpTUk0AAAAd/tenor.gif"
            cursor.execute("""
                INSERT INTO techniques (name, description, image, type, damages, accuracy, cost, cooldown)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Kamehameha', "Technique emblématique de l'univers de dragon ball.", kamehameha_gif, "kikoha",120,65,70,0))
            print("Technique 'kamehameha' ajouté à la table 'techniques'.")

            garric_gun_gif = "https://c.tenor.com/zof-eTe2ibwAAAAC/tenor.gif"
            cursor.execute("""
                INSERT INTO techniques (name, description, image, type, damages, accuracy, cost, cooldown)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, ('GarricGun', "Technique iconique des membres de la famille de vegeta.", garric_gun_gif, "kikoha",90,75,60,0))
            print("Technique 'garric gun' ajouté à la table 'techniques'.")

            kikoha_gif = "https://c.tenor.com/R11mg8c-5cwAAAAC/tenor.gif"
            cursor.execute("""
                INSERT INTO techniques (name, description, image, type, damages, accuracy, cost, cooldown)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Kikohas', "Attaques énergétiques à faible précision mais faible coût.", kikoha_gif, "kikoha",70,50,20,0))
            print("Technique 'Kikoha' ajouté à la table 'techniques'.")
            
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


def addStages(db_infos):
    try:
        db = mysql.connector.connect(
            host=db_infos['host'],
            user=db_infos['user'],
            password=db_infos['password'],
            database=db_infos['database']
        )
        cursor = db.cursor()

        # Vérifier si les personnages existent déjà dans la table
        cursor.execute("SELECT COUNT(*) FROM stages")
        stages_count = cursor.fetchone()[0]

        if stages_count == 0: 
            satan_city_image = "https://i.pinimg.com/originals/d0/5f/68/d05f68fe951d1a2a3e57774df5f1ba66.jpg"
            satan_city_icon = "https://i2.wp.com/retrodbzccg.com/wp-content/uploads/2014/04/satan-city.jpg?fit=320%2C240&ssl=1"
            cursor.execute("""
                INSERT INTO stages (name, description, type, image, icon)
                VALUES (%s, %s, %s, %s, %s)
            """, ("SatanCity", "La plus grande ville sur Terre", "solid",satan_city_image, satan_city_icon))
            print("Le Terrain 'satan_city' ajouté à la table 'stages'.")


            space_image = "https://pm1.aminoapps.com/7597/75f1b46b89157ca26e5c29c2603fadef8309a23fr1-1885-1080v2_hq.jpg"
            space_icon = "https://vgculturehq.com/wp-content/uploads/2018/10/dragon-ball-fighterz-ultimate-attack.jpg"
            cursor.execute("""
                INSERT INTO stages (name, description, type, image, icon)
                VALUES (%s, %s, %s, %s, %s)
            """, ("Espace", "Bah c'est l'espace quoi...", "solid",space_image, space_icon))
            print("Le Terrain 'space' ajouté à la table 'stages'.")

            
            db.commit()
        else:
            print("Les stages existent déjà dans la table 'stages'.")

        cursor.close()
        db.close()

    except mysql.connector.Error as error:
        db.rollback()
        print(f"Erreur: {error}")
        cursor.close()
        db.close()
