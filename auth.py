import json

def verify_user(username, password):
    with open("db.json", "r") as f:
        db = json.load(f)
    for user in db["usuarios"]:
        if user["username"] == username and user["password"] == password and user["vip"]:
            return True
    return False