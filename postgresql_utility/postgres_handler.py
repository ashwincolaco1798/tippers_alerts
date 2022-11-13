import psycopg2

from CONSTANTS import StatusCode


class PostGresHandler:
    _conn = psycopg2.connect(host = "caredex-db.ics.uci.edu", database = "tippersdb_uci", user = "postgres", password = "cAredEXpOstgrespW")
    
    _cursor = _conn.cursor()
    
    def insert_alert(self, query:str) -> tuple[StatusCode,str]:
        try:
            self._cursor.execute("INSERT INTO ALERTS(query, status) VALUES ({},{})".format(query,0)) # 0 for now is False
            return StatusCode.OK, "Inserted successfully"
        except:
            return StatusCode.INVALID, "Insert Failed"
    
    def execute_query(self, query:str) -> tuple[StatusCode, str]:
        try:
            result = self._cursor.execute(query)
            if result.rowcount > 0:
                self._cursor.execute("UPDATE ALARMS SET status = 1 WHERE query = {}", query)
        except:
            return StatusCode, "Query Failed to execute/Database error"