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

        cursor.execute("SELECT * FROM users WHERE nickname = 'Admin'")
        admin_exists = cursor.fetchone()

        if not admin_exists:
            cursor.execute("""
                INSERT INTO users (nickname, email, password, admin, profile_picture)
                VALUES (%s, %s, %s, %s, %s)
            """, ('Admin', 'admin@example.com', 'password123', True, "https://pm1.aminoapps.com/6513/7a6c57af2212845871e63e55f6cd476851ebebcd_00.jpg"))
            print("Utilisateur 'Admin' a été ajouté à la table 'users'.")
        else:
            print("L'utilisateur 'Admin' existe déjà.")

        cursor.execute("SELECT * FROM users WHERE nickname = 'Utilisateur'")
        user_exists = cursor.fetchone()

        if not user_exists:
            cursor.execute("""
                INSERT INTO users (nickname, email, password, admin,profile_picture,banner,current_quest_stage, experience, level)
                VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s)
            """, ('Utilisateur', 'user@example.com', 'password456', False, "https://i.pinimg.com/564x/b1/79/47/b17947cd9653a08b2801d11afd291d2d.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSr5STtRwhRGtjmno8wvhTi0rklpxHIe44Vj6bBRRV_syAfsdinpR3bTwBPYbE9BZEQ7-k&usqp=CAU",1,0,1))
            print("Utilisateur 'Utilisateur' a été ajouté à la table 'users'.")
        else:
            print("L'utilisateur 'Utilisateur' existe déjà.")

        db.commit()

        cursor.close()
        db.close()

    except mysql.connector.Error as error:
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
            """, ('Vegeta', 'Saiyan', vegeta_image, 'Fier prince des Saiyans.', 85, 85, 60, 1750, 750))
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
            print("Personnage 'Piccolo' ajouté à la table 'characters'.")


            goku_ssj1_image = "https://dragonball-legends.com/assets/characters/0563_gokuss1_563_texture/Texture2D/0563_GokuSS1_563_Chara_00.png"
            cursor.execute("""
                INSERT INTO characters (name, race, image, description, strength, defense, speed, health, energy)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Super Saiyan Goku', 'Saiyan', goku_ssj1_image, 'Première apparition d"un super Saiyan dans la série.', 95, 70, 70, 1500, 650))
            print("Personnage 'Goku ssj1' ajouté à la table 'characters'.")

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

            freezer_image = "https://dragonball-legends.com/assets/characters/0219_friezafp_219_texture/0219_FriezaFP_219_Chara.png"
            cursor.execute("""
                INSERT INTO characters (name, race, image, description, strength, defense, speed, health, energy)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Freezer (full power)', 'Démon du Givre', freezer_image, 'Créature impitoyable, terrifiant conquérant de la glaxie.', 90, 50, 65, 2200, 500))
            print("Personnage 'Freezer (full power)' ajouté à la table 'characters'.")

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

            normal_attack_gif = "https://i.gifer.com/77dr.gif"
            cursor.execute("""
                INSERT INTO techniques (name, description, image, type, damages, accuracy, cost, cooldown)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, ('NormalAttack', "Enchainnement de coups simple mais effiace.", normal_attack_gif, "normal_attack",50,95,20,0))
            print("Technique 'Normal Attack' ajouté à la table 'techniques'.")

            guard_gif = "https://c.tenor.com/0MAPePoGxQ4AAAAC/tenor.gif"
            cursor.execute("""
                INSERT INTO techniques (name, description, image, type, damages, accuracy, cost, cooldown)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Guard', "Technique defensive visant uniquement à bloquer une attaque.", guard_gif, "defense",0,90,50,2))
            print("Technique 'Guard' ajouté à la table 'techniques'.")

            counter_gif = "https://c.tenor.com/pbJ9Nuz-0y0AAAAC/tenor.gif"
            cursor.execute("""
                INSERT INTO techniques (name, description, image, type, damages, accuracy, cost, cooldown)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Counter', 'Attaque de contre qui à un gros risque d"échouer mais peut être très efficace.', counter_gif, 'counter_attack',0,60,50,4))
            print("Technique 'Counter' ajouté à la table 'techniques'.")


            kamehameha_gif = "https://c.tenor.com/DcU1rwpTUk0AAAAd/tenor.gif"
            cursor.execute("""
                INSERT INTO techniques (name, description, image, type, damages, accuracy, cost, cooldown)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Kamehameha', 'Technique emblématique de l"univers de dragon ball.', kamehameha_gif, 'special',120,65,70,0))
            print("Technique 'kamehameha' ajouté à la table 'techniques'.")

            garric_gun_gif = "https://c.tenor.com/zof-eTe2ibwAAAAC/tenor.gif"
            cursor.execute("""
                INSERT INTO techniques (name, description, image, type, damages, accuracy, cost, cooldown)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, ('GarricGun', "Technique iconique des membres de la famille de vegeta.", garric_gun_gif, "special",90,75,60,0))
            print("Technique 'garric gun' ajouté à la table 'techniques'.")

            kikoha_gif = "https://c.tenor.com/R11mg8c-5cwAAAAC/tenor.gif"
            cursor.execute("""
                INSERT INTO techniques (name, description, image, type, damages, accuracy, cost, cooldown)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, ('Kikohas', "Attaques énergétiques à faible précision mais faible coût.", kikoha_gif, "special",70,50,20,0))
            print("Technique 'Kikoha' ajouté à la table 'techniques'.")

            charge_ki_gif = "https://c.tenor.com/i-580TEI3LoAAAAC/tenor.gif"
            cursor.execute("""
                INSERT INTO techniques (name, description, image, type, damages, accuracy, cost, cooldown)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, ('ChargeKi', "Technique consistant à augmenter son énergie temporairement.", charge_ki_gif, "chargeKi",0,100,0,0))
            print("Technique 'ChargeKi' ajouté à la table 'techniques'.")
            
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


def linkTechniquesToCharacter(db_infos):
    try:
        db = mysql.connector.connect(
            host=db_infos['host'],
            user=db_infos['user'],
            password=db_infos['password'],
            database=db_infos['database']
        )
        cursor = db.cursor()

        # Vérifier si les personnages existent déjà dans la table
        cursor.execute("SELECT COUNT(*) FROM technique_own_by")
        techLinked = cursor.fetchone()[0]

        if techLinked == 0:


            # cursor.execute("""
            #     INSERT INTO technique_own_by (idCharacter, idTechnique)
            #     VALUES (%s, %s)
            # """, ("vegeta_id", "normalAttack"))
            # print(f"NormalAttack Linked to vegeta")

            cursor.execute("SELECT idCharacter, name FROM characters")
            all_characters_ids = cursor.fetchall()
            all_characters_ids_dico = {}
            
            for id_char,name in all_characters_ids:
                all_characters_ids_dico[name] = id_char
            
            print(all_characters_ids_dico)

            cursor.execute("SELECT idTechnique, name FROM techniques")
            all_techniques_ids = cursor.fetchall()
            all_techniques_ids_dico = {}

            for id_char,name in all_techniques_ids:
                all_techniques_ids_dico[name] = id_char
            
            print(all_techniques_ids_dico)
            default_tech = ['NormalAttack', 'Guard', 'Counter', 'ChargeKi']

            for character in all_characters_ids_dico:
                for tech_to_link in default_tech:
                    cursor.execute("""
                        INSERT INTO technique_own_by (idCharacter, idTechnique)
                        VALUES (%s, %s)
                    """, (all_characters_ids_dico[character], all_techniques_ids_dico[tech_to_link]))
                    print(f"{tech_to_link} Linked to {all_characters_ids_dico[character]}")

            db.commit()
        else:
            print("Techniques Linked to their characters.")

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

        cursor.execute("SELECT COUNT(*) FROM stages")
        stages_count = cursor.fetchone()[0]

        if stages_count == 0: 
            satan_city_image = "https://i.pinimg.com/originals/d0/5f/68/d05f68fe951d1a2a3e57774df5f1ba66.jpg"
            satan_city_icon = "https://i.pinimg.com/originals/d0/5f/68/d05f68fe951d1a2a3e57774df5f1ba66.jpg"
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

            namek_lava_icon = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvpnZdXBaCT95m2bbdCtwCeI2Zro9mPy5MluJBjcMMz-q3cxnrqXH75d-0h3pZx1modRNpS-x_UuqU33Fan0TniDjHYZIn2bpncHZdgkE9U9bdqWj40NO2WIpVogOK_HgOFnL_bd5YNj8W/s1600/dbz106-01.jpg"
            namek_lava_image = "https://cdn.gamedevmarket.net/wp-content/uploads/20230107071946/dca48e4e74b9bc8bb861f577fef38a08.jpg"
            cursor.execute("""
                INSERT INTO stages (name, description, type, image, icon)
                VALUES (%s, %s, %s, %s, %s)
            """, ("namekLava", "Namek En Fusion", "solid",namek_lava_image, namek_lava_icon))
            print("Le Terrain 'namekLava' ajouté à la table 'stages'.")

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


def addQuestLevels(db_infos):
    try:
        db = mysql.connector.connect(
            host=db_infos['host'],
            user=db_infos['user'],
            password=db_infos['password'],
            database=db_infos['database']
        )
        cursor = db.cursor()

        cursor.execute("SELECT COUNT(*) FROM quest_levels")
        stages_count = cursor.fetchone()[0]

        if stages_count == 0: 
            
            cursor.execute("""
                INSERT INTO quest_levels (levelName, idPlayerCharacter, idEnemyCharacter, StageName, experience_earned, difficulty)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, ("Le Début d'une aventure", 1,7,"SatanCity",50,10))
            print("Niveau 1 Ajouté à la table : quest_levels")

            cursor.execute("""
                INSERT INTO quest_levels (levelName, idPlayerCharacter, idEnemyCharacter, StageName, experience_earned, difficulty)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, ("Le Prince des Saiyans", 1,2,"SatanCity",80,5))
            print("Niveau 2 Ajouté à la table : quest_levels")

            cursor.execute("""
                INSERT INTO quest_levels (levelName, idPlayerCharacter, idEnemyCharacter, StageName, experience_earned, difficulty)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, ("Le Super Saiyan Légendaire", 5,8,"namekLava",200,1))
            print("Niveau 3 Ajouté à la table : quest_levels")

            cursor.execute("""
                INSERT INTO quest_levels (levelName, idPlayerCharacter, idEnemyCharacter, StageName, experience_earned, difficulty)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, ("Affrontement père adoptif, fils. ", 3,4,"SatanCity",30,2))
            print("Niveau 4 Ajouté à la table : quest_levels")

            db.commit()
        else:
            print("Les niveaux existent déjà dans la table 'quest_levels'")

        cursor.close()
        db.close()

    except mysql.connector.Error as error:
        db.rollback()
        print(f"Erreur: {error}")
        cursor.close()
        db.close()