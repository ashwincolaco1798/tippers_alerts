import CONSTANTS

def tipper_logs(message: str):
    if CONSTANTS.LOG_MODE:
        print("[TIPPERS-LOGS]: " + message)