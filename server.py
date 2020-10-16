from flask import Flask, Response, request
import pymongo
import json
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoClientの作成, MongoDBへの接続
try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS=1000,
    )
    db = mongo.company
    # print(mongo.server_info())

except Exception as e:
    print("ERROR - Cannot connect to db", e)


# API routing

# ユーザー一覧の取得
@app.route("/users", methods=["GET"])
def get_users():
    try:
        db_response = list(db.users.find())

        for user in db_response:
            user["_id"] = str(user["_id"])

        return Response(
            response=json.dumps(
                db_response
            ),
            status=200,
            mimetype="application/json",
        )

    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({
                "message": "Could not read users",
            }),
            status=500,
            mimetype="application/json",
        )


# ユーザー情報の登録
@app.route("/users", methods=["POST"])
def create_user():
    try:
        # user = {"name": "FirstName", "lastName": "LastName"}
        user = {
            "name": request.form["name"],
            "lastName": request.form["lastName"],
        }

        db_response = db.users.insert_one(user)

        return Response(
            response=json.dumps({
                "message": "Created : user",
                "id": f"{db_response.inserted_id}",
            }),
            status=200,
            mimetype="application/json",
        )

    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({
                "message": "Could not create a user",
            }),
            status=500,
            mimetype="application/json",
        )


# ユーザー情報の更新
@app.route("/users/<id_>", methods=["PATCH"])
def update_user(id_):
    try:
        _id = {"_id": ObjectId(id_)}

        result_get_one = db.users.find_one(_id)
        print(result_get_one["name"])

        result_update = db.users.update_one(
            _id,
            {
                "$set": {
                    "name": request.form["name"],
                    "lastName": request.form["lastName"],
                }
            }
        )

        # for attr in dir(result_update):
        #     print(f"***{attr}***")

        print(result_update.modified_count)

        if result_update.modified_count == 1:
            return Response(
                response=json.dumps(
                    {
                        "message": "Updated : user",
                        "name_before": result_get_one["name"],
                        "lastName_before": result_get_one["lastName"],
                        "name_after": request.form["name"],
                        "lastName_after": request.form["lastName"],
                    }
                ),
                status=200,
                mimetype="application/json",
            )
        else:
            return Response(
                response=json.dumps(
                    {
                        "message": "nothing to update",
                    }
                ),
                status=200,
                mimetype="application/json",
            )

    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "Could not update user"}),
            status=500,
            mimetype="application/json",
        )


if __name__ == "__main__":
    app.run(port=80, debug=True)
