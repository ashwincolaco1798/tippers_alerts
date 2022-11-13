from email import header
import pandas as pd
import time
from postgresql_utility import postgres_handler
from tippers_logs import logger
import CONSTANTS
queries_df = pd.DataFrame(columns= ['query','interval', 'time_remaining', 'cumulative_time'])

pgh = postgres_handler.PostGresHandler()

def query_scheduling():
    while 1:
        service = queries_df.sort_values(by = ['time_remaining']).loc[queries_df['time_remaining']<=0]
        start = time.time()
        for query in service["query"]:
            if(service['query']['cumulative_time']>time.time()):
                code, err = pgh.execute_query(query)
                logger.tipper_logs(err)
        queries_df.loc[queries_df['time_remaining']<=0] = 9999
        queries_df.loc[queries_df['time_remaining']>0] = queries_df['time_remaining'] - (time.time() - start)
        queries_df.loc[queries_df['time_remaining']>999] = queries_df['interval']
    


