from enum import Enum

LOG_MODE = True
class StatusCode(Enum):
    NOT_FOUND = -1
    OK = 0
    INVALID = 1
    UNAUTHORIZED = 2


