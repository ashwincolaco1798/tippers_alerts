import psycopg2


class PostGresUtility:
    _conn = psycopg2.connect(host = "caredex-db.ics.uci.edu", database = "tippersdb_uci", user = "postgres", password = "cAredEXpOstgrespW")
    
    _cursor = _conn.cursor()
    
    def insert_alert(self, query:str):
        self._cursor.execute("INSERT INTO ALERTS(query, status) VALUES ({},{})".format(query,0)) # 0 for now is False
        