import psycopg2


class PostGresUtility:
    conn = psycopg2.connect(host = "caredex-db.ics.uci.edu", database = "tippersdb_uci", user = "postgres", password = "cAredEXpOstgrespW")
