import mysql.connector

def createUserTable(db_infos):
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )
    cursor = db.cursor()

    cursor.execute("SHOW TABLES LIKE 'users'")
    result = cursor.fetchone()

    if not result:
        cursor.execute("""
                CREATE TABLE users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nickname VARCHAR(255),
                    bio TEXT,
                    email VARCHAR(255),
                    password VARCHAR(255),
                    admin BOOLEAN,
                    profile_picture TEXT,
                    banner TEXT,
                    favorite_character VARCHAR(255),
                    collection_id INT,
                    current_quest_stage INT,
                    experience FLOAT,
                    level INT
                )
            """)
        print("La table 'users' a été créée avec succès.")
    else:
        print("La table 'users' existe déjà.")
    
    cursor.close()
    db.close()


def createCharacterTable(db_infos):
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )
    cursor = db.cursor()


    # cursor.execute("DROP TABLE `characters`")

    cursor.execute("SHOW TABLES LIKE 'characters'")
    result = cursor.fetchone()

    if not result:
        cursor.execute("""
                CREATE TABLE characters (
                    idCharacter INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    race VARCHAR(255),
                    image TEXT,
                    description TEXT,
                    strength INT,
                    defense INT,
                    speed INT,
                    health INT,
                    energy INT
                )
            """)
        print("La table 'characters' a été créée avec succès.")
    else:
        print("La table 'characters' existe déjà.")
    
    cursor.close()
    db.close()


def createTechniqueTable(db_infos):
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )
    cursor = db.cursor()

    cursor.execute("SHOW TABLES LIKE 'techniques'")
    result = cursor.fetchone()

    if not result:
        cursor.execute("""
                CREATE TABLE techniques (
                    idTechnique INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    description TEXT,
                    image TEXT,
                    type VARCHAR(255),
                    damages INT,
                    accuracy INT,
                    cost INT,
                    cooldown INT
                )
            """)
        print("La table 'techniques' a été créée avec succès.")
    else:
        print("La table 'techniques' existe déjà.")
    
    cursor.close()
    db.close()


def createTechniqueOwnByeTable(db_infos):
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )
    cursor = db.cursor()

    cursor.execute("SHOW TABLES LIKE 'technique_own_by'")
    result = cursor.fetchone()

    if not result:
        cursor.execute("""
                CREATE TABLE technique_own_by (
                    idCharacter INT,
                    idTechnique INT                    
                )
            """)
        print("La table 'technique_own_by' a été créée avec succès.")
    else:
        print("La table 'technique_own_by' existe déjà.")
    
    cursor.close()
    db.close()



def createQuestLevelsTable(db_infos):
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )
    cursor = db.cursor()

    cursor.execute("SHOW TABLES LIKE 'quest_levels'")
    result = cursor.fetchone()

    if not result:
        cursor.execute("""
                CREATE TABLE quest_levels (
                    idLevel INT AUTO_INCREMENT PRIMARY KEY,
                    levelName TEXT,
                    idPlayerCharacter INT,
                    idEnemyCharacter INT,
                    StageName TEXT,
                    experience_earned FLOAT
                )
            """)
        print("La table 'quest_levels' a été créée avec succès.")
    else:
        print("La table 'quest_levels' existe déjà.")
    
    cursor.close()
    db.close()


def createStageTable(db_infos):
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )
    cursor = db.cursor()

    cursor.execute("SHOW TABLES LIKE 'stages'")
    result = cursor.fetchone()

    if not result:
        cursor.execute("""
                CREATE TABLE stages (
                    idStage INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    description TEXT,
                    type VARCHAR(255),    
                    image TEXT,
                    icon TEXT              
                )
            """)
        print("La table 'stages' a été créée avec succès.")
    else:
        print("La table 'stages' existe déjà.")
    
    cursor.close()
    db.close()