import mariadb
from flask import Flask, json, request, Response
from werkzeug.wrappers import response
import sys
import json

app = Flask(__name__)


#mysite.ml/users.html
#mysite.ml/api/=> http://127.0.0.1:5000/api
@app.route("/api")
def home():
    return "Hello world"

@app.route("/api/fruit", methods= ['GET', 'POST', 'PATCH'])
def fruit():
    fruit_name = "dragonfruit"
    if request.method == 'GET':
        resp = {
            "fruitName" : fruit_name
        }
        return Response (json.dumps(resp),
                        mimetype="application/json",
                        status=200
                        )
    elif request.method == 'POST':
        data = request.json
        print(data)
        if (data.get('fruitName') != None):
            resp = "Wrong fruit"
            code = 400
            
            if (data.get('fruitname') == fruit_name):
                resp = "Correct fruit"
                code = 201
            return Response (resp,
                            mimetype="text/plain",
                            status=code)
        else:
            return Response ("Error, missing arguments",
                        mimetype="text/plain",
                        status=400
                        )    

    elif request.method == 'PATCH':
        return Response ("Endpoint under mantaince",
                        mimetype="text/plain",
                        status=503)
    else:
        print("Something went wrong")
    
if (len(sys.argv) > 1):
    mode = sys.argv[1]
    if (mode == "production"):
        import bjoern
        host = '0.0.0.0'
        port = 5000
        print("Server is running in production mode")
        bjoern.run(app, host, port)
    elif(mode == "testing"):
        from flask_cors import CORS
        CORS(app)
        print("Server is running in testing mode, switch to production when needed")
        app.run(debug=True)
    else:
        print("Invalid mode argement, exiting")
        exit()
    
else:
    print("No arrgements")
    exit()
    