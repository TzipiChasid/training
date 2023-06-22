from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""
@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})

@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route('/users',methods=["GET"])
def getUserByTeam():
    if request.args.get('team'):
        return create_response({"users":(list(filter(lambda key: key['team']==request.args.get('team') ,db.get('users'))))})
    return create_response({"users":db.get('users')},200,'I get users')

@app.route('/users/<int:id>',methods=["GET"])
def getUserById(id):
    if(db.getById('users', id) is None):
            return create_response(None,404,"The id did not found")
    return create_response({"users":db.getById('users', id)},200,'The object updated')

@app.route('/users/payload',methods=["POST"])
def addUser(): 
    objectJson = request.get_json()
    if("name" in objectJson and "age" in objectJson and "team" in objectJson and len((list(filter(lambda key:objectJson[key]!="" ,objectJson))))==3):
        {"users":db.create("users",objectJson)}   
        return create_response(objectJson,200,"The object updated")
    return create_response(objectJson,404,"You did not send a valid request")

@app.route('/users/<int:id>',methods=["PUT"])
def PutUserById(id):
    objectJson = request.get_json()
    if("name" in objectJson and "age" in objectJson and "team" in objectJson and len((list(filter(lambda key:objectJson[key]!="" ,objectJson))))==3):
        db.updateById("users",id,objectJson)
        return create_response(objectJson,200,"The object updated")
    return create_response(objectJson,404,"You did not send a valid request")

@app.route('/users/<int:id>',methods=["DELETE"])
def DeleteUserById(id):
    if(db.getById('users', id) is None):
        return create_response(None,404,"The id did not found")
    db.deleteById("users",id)
    return create_response(None,200,"The object delete")

# TODO: Implement the rest of the API here!

"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(debug=True)
