import json
import os

class Config:
    def check():
        if not os.path.isdir("data"):
            os.mkdir("data")

        if not os.path.isfile("data/config.json"):
            with open("data/config.json", "w") as f:
                json.dump({"upload_dir": "files/", "auth_token": "securepassword"}, f)

    def change_auth_token(new_auth_token):
        data = json.load(open("data/config.json"))
        data["auth_token"] = new_auth_token
        json.dump(data, open("data/config.json", "w"))

    def get_upload_dir():
        return str(json.load(open("data/config.json"))["upload_dir"])

    def get_auth_token():
        return str(json.load(open("data/config.json"))["auth_token"])
