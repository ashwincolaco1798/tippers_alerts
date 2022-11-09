from CONSTANTS import StatusCode

def verify_payload(payload: dict, requirements: list[str]) -> tuple[StatusCode, str]:
    for requirement in requirements:
        if requirement not in payload:
            return StatusCode.NOT_FOUND, requirement
    return StatusCode.OK, "All G"