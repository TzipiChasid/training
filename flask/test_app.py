from flask import json
# pytest automatically injects fixtures
# that are defined in conftest.py
# in this case, client is injected
def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.json["result"]["content"] == "hello world!"

def test_mirror(client):
    res = client.get("/mirror/Tim")
    assert res.status_code == 200
    assert res.json["result"]["name"] == "Tim"

def test_get_users(client):
    res = client.get("/users")
    assert res.status_code == 200
    res_users = res.json["result"]["users"]
    assert len(res_users) == 4
    assert res_users[0]["name"] == "Aria"

def tests_get_users_with_team(client):
    res = client.get("/users?team=LWB")
    assert res.status_code == 200
    res_users = res.json["result"]["users"]
    assert len(res_users) == 2
    assert res_users[1]["name"] == "Tim"

def test_get_user_id(client):
    res = client.get("/users/1")
    assert res.status_code == 200
    res_user = res.json["result"]["users"]
    assert res_user["name"] == "Aria"
    assert res_user["age"] == 19

def test_add_user(client):
    obj={"name":"gil","age":3,"team":"ptc"}
    res=client.post('/users/payload',data=json.dumps(obj),headers={'Content-Type':'application/json'})
    assert res.status_code == 200
    res_users = res.json["result"]
    assert res.json["message"] == "The object updated"
    assert res_users["age"] == 3
    assert res_users["id"] == 5
    assert res_users["name"] == "gil"
    assert res_users["team"] == "ptc"
    assert res.json["success"] == True

def test_put_user_by_id(client):
    obj={"name":"gil","age":3,"team":"ptc"}
    res=client.put('/users/1',data=json.dumps(obj),headers={'Content-Type':'application/json'})
    assert res.status_code == 200
    res_users = res.json["result"]
    assert res.json["message"] == "The object updated"
    assert res_users["age"] == 3
    assert res_users["name"] == "gil"
    assert res_users["team"] == "ptc"
    assert res.json["success"] == True

def test_delete_user_by_id(client):
    res=client.delete("/users/1")
    assert res.status_code == 200
    assert res.json["message"]  == "The object delete"

def test_get_user_id_404(client):
    res = client.get("/users/0")
    assert res.status_code == 404
    assert res.json["message"]== "The id did not found"
    assert res.json["result"]==None
    assert res.json["success"] == False

def test_add_user_404(client):
    obj={"age":3,"name":"","team":"ptc"}
    res = client.post("/users/payload",data=json.dumps(obj),headers={'Content-Type':'application/json'})
    assert res.status_code == 404
    res_users = res.json["result"]
    assert res.json["message"] == "You did not send a valid request"
    assert res_users["age"] == 3
    assert res_users["name"] == ""
    assert res_users["team"] == "ptc"
    assert res.json["success"] == False
    
def test_put_user_by_id_404(client):
    obj={"name":"","age":3,"team":"ptc"}
    res = client.put("/users/1",data=json.dumps(obj),headers={'Content-Type':'application/json'})
    assert res.status_code == 404
    res_users = res.json["result"]
    assert res.json["message"] == "You did not send a valid request"
    assert res_users["age"] == 3
    assert res_users["name"] == ""
    assert res_users["team"] == "ptc"
    assert res.json["success"] == False

def test_delete_user_by_id_404(client):
    obj={"name":"gil","age":3,"team":"ptc"}
    res = client.delete("/users/0")
    assert res.status_code == 404
    assert res.json["message"] == "The id did not found"

   