
from flask import Flask
import json
app = Flask(__name__)

@app.route('/')
def hello():
    print('hello')
    return ' Hello World! I have been seen '

@app.route('/capsules/all')
def all():
    with open('capsules.json') as dataFromJson:
        data = json.load(dataFromJson)
    return data 


@app.route('/capsules/<string:name>')
def getName(name):
    with open('capsules.json') as dataFromJson:
        data = json.load(dataFromJson)
        for searchName in data:
            if (searchName['name'] == name):
                answer=searchName
    return answer;        

@app.route('/capsules/<int:id>')
def getName(id):
    with open('capsules.json') as dataFromJson:
        data = json.load(dataFromJson)
        for searchId in data:
            if (searchId[id] == id):
                answer=searchId
    return answer;        
if __name__ == "__main__":
    app.run(debug=True)

     