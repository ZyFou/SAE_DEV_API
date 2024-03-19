# flask run --debug

from flask import Flask, jsonify, request
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sae_api"
)

cursor = db.cursor()


from utils import createTables  
createTables.createUserTable(cursor)


from utils import addExempleUsers

addExempleUsers.addExempleUsers(cursor, db)

cursor.close()
db.close()



db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sae_api"
)

app = Flask(__name__)

@app.route('/api/infos/<string:prenom>', methods=['GET'])
def obtenir_donnees(prenom):
    cursor = db.cursor()
    query = "SELECT * FROM `users` WHERE prenom = %s"
    cursor.execute(query, (prenom,))
    result = cursor.fetchall()

    if len(result) == 0:
        return jsonify({"message": "Utilisateur non trouvé"}), 404

    columns = [col[0] for col in cursor.description]

    user_data = {}
    for i, col in enumerate(columns):
        forbiden_col = ["password"]
        if not col in forbiden_col:
            user_data[col] = result[0][i]

    return jsonify(user_data)


if __name__ == '__main__':
    app.run(debug=True)