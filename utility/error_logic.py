from CONSTANTS import StatusCode
from flask import jsonify, Response
def handle_error_logic(status_code: StatusCode, err_msg="") -> Response:
    if err_msg == "":
        return jsonify(
            {
                'status_code': status_code.value
            }
        )
    return jsonify(
        {
            'status_code': status_code.value,
            'message': err_msg
        }
    )
