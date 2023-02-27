from flask import Flask
import json
import main

app = Flask(__name__)

@app.route('/devices', methods=['GET'])
def devices():
    print(main.last_run)
    return json.dumps(
        {
            "success": True,
            "status": 200,
            "data": {
                "devices": main.devices,
                "last_run": main.last_run,
                "last_ping": main.last_ping
            }
        })

@app.errorhandler(404)
def not_found(error):
    return json.dumps(
        {
            "success": False,
            "status": 404,
            "error": "NOT_FOUND"

        }
    ), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return json.dumps(
        {
            "success": False,
            "status": 405,
            "error": "METHOD_NOT_ALLOWED"

        }
    ), 405

@app.errorhandler(500)
def internal_server_error(error):
    print(error)
    return json.dumps(
        {
            "success": False,
            "status": 500,
            "error": "INTERNAL_SERVER_ERROR"

        }
    ), 500


app.run(host='127.0.0.1', port=5000)