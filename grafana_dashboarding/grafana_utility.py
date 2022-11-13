from CONSTANTS import StatusCode

import json

class GrafanaHandler:

    _panel = json.load(open("grafana_panel.json","r"))
    _dashboard = json.load(open("grafana_dashboard.json","r"))
    def add_panel(query_desc: str, query: str)-> tuple[StatusCode, str]:
        return

