import flask

class Tweet:
    val = ""

t = Tweet()
app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/tweet', methods=['GET'])
def getTweet():
    return {
        "status": "ok",
        "id": t.val,
    }


@app.route('/tweet/<id>', methods=['PUT'])
def setTweet(id):
    t.val = id
    return {
        "status": "ok",
        "id": t.val,
    }


app.run()
