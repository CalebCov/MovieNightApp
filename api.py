# this file is where all the api routes are to query the database

from flask import Blueprint, jsonify
from flask import request
from db_connection import dbConnection

# the Blueprint class allows you to organize routes, views, and other modular structures. Helps to create scalable and maintainable Flask apps.
api = Blueprint('api', __name__)


# request to return all names in the friends table.
@api.route('/api/friends', methods=['GET'])
def friend_list():
    connection = dbConnection()
    cursor = connection.cursor(dictionary=True)
    sql_query = "SELECT firstname, lastname FROM friend"
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    return jsonify(rows)

# request to delete a friend from the friends table
@api.route('/api/removefriend/<int:id>', methods = ['DELETE'])
def remove_friend(id):
    connection = dbConnection()
    cursor = connection.cursor(dictionary=True)

    # get the name before deleting
    select_query = "SELECT firstname, lastname FROM friend WHERE id = %s"
    cursor.execute(select_query, (id,))
    friend = cursor.fetchone()

    # delete the friend
    delete_query = "DELETE FROM friend WHERE id = %s"
    cursor.execute(delete_query, (id,))
    connection.commit()

    if friend:
        message = "{} {} has been removed".format(friend['firstname'], friend['lastname'])
        return jsonify(message=message)
    else:
        return jsonify(message="User not found")
    
# request to add a freind to the friends table
@api.route('/api/addfriend', methods = ['POST'])
def add_friend():
    data = request.get_json()
    firstname = data ['firstname']
    lastname = data['lastname']

    connection = dbConnection()
    cursor = connection.cursor()
    sql_qurey = "INSERT INTO friend (firstname, lastname) VALUES (%s, %s)"
    cursor.execute(sql_qurey, (firstname, lastname))
    connection.commit()

    return jsonify(message ="Welcome {} {} to Movie Night.".format(firstname, lastname))

# request to update a friends data
@api.route('/api/updatefriend/<int:id>', methods = ['PUT'])
def update_friend(id):
    data = request.get_json()
    new_firstname = data.get('firstname')
    new_lastname = data.get('lastname')

    connection = dbConnection()
    cursor = connection.cursor(dictionary=True)

# if statements give you the option to update names separately
    if new_firstname:
        sql_query = "UPDATE friend SET firstname = %s WHERE id = %s"
        cursor.execute(sql_query, (new_firstname, id))
   
    if new_lastname:
        sql_query = "UPDATE friend SET lastname = %s WHERE id =%s"
        cursor.execute(sql_query, (new_lastname, id))

    connection.commit()

    return jsonify(messeage="Name updated successfully.")