# flask run --debug

from flask import Flask, jsonify, request
import mysql.connector

db_infos = {"host" : "localhost", "user":"root", "password":"", "database":"sae_api"}


from utils import createTables  
createTables.createUserTable(db_infos)
createTables.createCharacterTable(db_infos)
createTables.createTechniqueTable(db_infos)
createTables.createTechniqueOwnByeTable(db_infos)
createTables.createStageTable(db_infos)



from utils import addDataToDB
addDataToDB.addExempleUsers(db_infos)
addDataToDB.addCharacters(db_infos)
addDataToDB.addTechniques(db_infos)
addDataToDB.addStages(db_infos)

addDataToDB.linkTechniquesToCharacter(db_infos)


app = Flask(__name__)

@app.route('/api/userInfos/<int:id>', methods=['GET'])
def get_users_data(id):
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )

    cursor = db.cursor()
    query = "SELECT * FROM `users` WHERE id = %s"
    cursor.execute(query, (id,))
    result = cursor.fetchall()

    if len(result) == 0:
        return jsonify({"message": "Utilisateur non trouvé"}), 404

    columns = [col[0] for col in cursor.description]

    user_data = {}
    for i, col in enumerate(columns):
        forbiden_col = ["password", "admin","email"]
        if not col in forbiden_col:
            user_data[col] = result[0][i]

    cursor.close()
    db.close()
    return jsonify(user_data)


@app.route('/api/characters/', methods=['GET'])
def get_characters():
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )

    cursor = db.cursor()
    query = "SELECT * FROM `characters`"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    if len(result) == 0:
        return jsonify({"message": "Aucun personnages"}), 404


    characters = [{"name": row[1], "race": row[2], "image":row[3]} for row in result]
    return jsonify({"characters": characters})


@app.route('/api/characters/<string:name>', methods=['GET'])
def get_specific_character(name):
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )

    cursor = db.cursor()
    query = "SELECT * FROM `characters` WHERE name = %s"
    cursor.execute(query, (name,))
    result = cursor.fetchall()

    if len(result) == 0:
        return jsonify({"message": "Personnage inconnu"}), 404

    columns = [col[0] for col in cursor.description]

    user_data = {}
    for i, col in enumerate(columns):
        user_data[col] = result[0][i]

    return jsonify(user_data)


@app.route('/api/techniques/', methods=['GET'])
def get_techniques():
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )

    cursor = db.cursor()
    query = "SELECT * FROM `techniques`"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    if len(result) == 0:
        return jsonify({"message": "Aucune technique"}), 404


    techniques = [{"name": row[1], "Description": row[2], "type": row[3]} for row in result]
    return jsonify({"techniques": techniques})

@app.route('/api/techniques/<string:name>', methods=['GET'])
def get_specific_technique(name):
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )

    cursor = db.cursor()
    query = "SELECT * FROM `techniques` WHERE name = %s"
    cursor.execute(query, (name,))
    result = cursor.fetchall()

    if len(result) == 0:
        return jsonify({"message": "Technique inconnue"}), 404

    columns = [col[0] for col in cursor.description]

    technique_data = {}
    for i, col in enumerate(columns):
        technique_data[col] = result[0][i]

    return jsonify(technique_data)

@app.route('/api/stages/', methods=['GET'])
def get_stages():
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )

    cursor = db.cursor()
    query = "SELECT * FROM `stages`"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    if len(result) == 0:
        return jsonify({"message": "Aucun terrain"}), 404
    
    stages = [{"name": row[1], "Description": row[2], "type": row[3], "icon" : row[5]} for row in result]
    return jsonify({"stages": stages})

@app.route('/api/stages/<string:name>', methods=['GET'])
def get_specific_stages(name):
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )

    cursor = db.cursor()
    query = "SELECT * FROM `stages` WHERE name = %s"
    cursor.execute(query, (name,))
    result = cursor.fetchall()

    if len(result) == 0:
        return jsonify({"message": "Terrain introuvable"}), 404
    
    columns = [col[0] for col in cursor.description]
    stage_data = {}

    for i, col in enumerate(columns):
        stage_data[col] = result[0][i]
        
    return jsonify(stage_data)


if __name__ == '__main__':
    app.run(debug=True)