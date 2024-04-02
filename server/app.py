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


    techniques = [{"idTechnique": row[0],"name": row[1], "Description": row[2], "type": row[3]} for row in result]
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

@app.route('/api/techniques/<int:idTechnique>', methods=['GET'])
def get_specific_technique_id(idTechnique):
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )

    cursor = db.cursor()
    query = "SELECT * FROM `techniques` WHERE idTechnique = %s"
    cursor.execute(query, (idTechnique,))
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

@app.route('/api/TOB/', methods=['GET'])
def get_techniques_linked():
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )

    cursor = db.cursor()
    query = "SELECT * FROM `technique_own_by` "
    cursor.execute(query)
    results = cursor.fetchall()
    
    if len(results) == 0:
        return jsonify({"message": "Aucun Id Trouvé"}), 404

    TOB_Data = {}
    for row in results:
        idCharacter = row[0]
        idTechnique = row[1]

        if idCharacter not in TOB_Data:
            TOB_Data[idCharacter] = []

        TOB_Data[idCharacter].append(idTechnique)

    # Convertir TOB_Data en une liste de dictionnaires
    TOB_List = [{"idCharacter": k, "idTechniques": v} for k, v in TOB_Data.items()]

    return jsonify(TOB_List)




@app.route('/api/TOB/<int:idCharacter>', methods=['GET'])
def get_infos_techniques_linked(idCharacter):
    db = mysql.connector.connect(
        host=db_infos['host'],
        user=db_infos['user'],
        password=db_infos['password'],
        database=db_infos['database']
    )

    cursor = db.cursor()

    query = "SELECT idTechnique FROM `technique_own_by` WHERE idCharacter = %s"
    cursor.execute(query, (idCharacter,))
    results = cursor.fetchall()

    if len(results) == 0:
        return jsonify({"message": "Aucune technique associée"}), 404

    # Créer une liste pour stocker les idTechnique
    idTechniques = [row[0] for row in results]

    # Vous pouvez retourner directement la liste d'idTechniques
    return jsonify({"idCharacter": idCharacter, "idTechniques": idTechniques})







if __name__ == '__main__':
    app.run(debug=True)