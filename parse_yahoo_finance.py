import requests
from datetime import datetime
import json


end_ts = str(int(datetime.timestamp(datetime.today())))
parameters = {'period1':'0','period2':end_ts,'interval':'1d','events':'history'}
headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
tickers = ['PD','ZUO','PINS','ZM','PVTL','DOCU','CLDR','RUN']

def get_json_data(tickers,headers,parameters,end_ts):
    data = {}
    for t in tickers:
        url = 'https://query1.finance.yahoo.com/v7/finance/download/{}?'.format(t)
        r = requests.get(url,headers=headers,params=parameters)
        stock_data = []
        keys = r.text.split(sep='\n')[0].split(sep=',')
        for i in r.text.split(sep='\n')[1:]:
            dic = dict()
            for i,k in enumerate(i.split(sep=',')):
                dic[keys[i]]=k
            stock_data.append(dic)
        data[t] = stock_data
    return json.dumps(data,indent=4)


if __name__ == "__main__":
    data = get_json_data(tickers,headers,parameters,end_ts)
    # with open('data.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f)
    