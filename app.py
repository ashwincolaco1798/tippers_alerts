from cmath import log
from flask import Flask, jsonify, request
from flask_cors import CORS

from CONSTANTS import StatusCode
from utility import verifier, error_logic
from grafana_dashboarding import grafana_utility
from tippers_logs import logger
from postgresql_utility import postgres_handler
from scheduler import query_scheduler

app = Flask(__name__, instance_relative_config=True)

CORS(app)


pgh = postgres_handler.PostGresHandler()
gfu = grafana_utility.GrafanaHandler()

@app.route('/create_alert', methods = ['POST'])
def create_alert():
    payload = request.json
    code, err = verifier.verify_payload(payload,['query_description','query','interval','recurrence'])
    if code != StatusCode.OK:
        error_logic.handle_error_logic(code,err)

    code, err = pgh.insert_alert(payload['query_description'])
    if(code!= StatusCode.OK):
        return error_logic.handle_error_logic(code,err)
    
    code, err = gfu.add_panel(payload['query_description'], payload['query'])



if __name__ == "__main__":
    query_scheduler.query_scheduling()
    app.run(host='0.0.0.0')

    

    
    
    
    
