from cmath import log
from flask import Flask, jsonify, request
from flask_cors import CORS

from CONSTANTS import StatusCode
from payload_verification import verifier
from grafana_dashboaring import grafana_utility
from tippers_logs import logger
from postgresql_utility import connection

postgres_conn = connection.PostGresUtility()

app = Flask(__name__, instance_relative_config=True)

CORS(app)



@app.route('/create_alert', methods = ['POST'])
def create_alert():
    payload = request.json
    code, err = verifier.verify_payload(payload,['query','frequency','recurrence','end_time'])
    if code != StatusCode.OK:
        logger.tipper_logs(err)
    
    
    
    
