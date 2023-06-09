# this file is where all the api routes are to query the database

from flask import Blueprint, jsonify
from db_connection import dbConnection

# the Blueprint class allows you to organize routes, views, and other modular structures. Helps to create scalable and maintainable Flask apps.
api = Blueprint('api', __name__)


# request to return all names in the friends table.
@api.route('/friends', methods=['GET'])
def friend_list():
    connection = dbConnection()
    cursor = connection.cursor(dictionary=True)
    sql_query = "SELECT * FROM friend"
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    return jsonify(rows)
