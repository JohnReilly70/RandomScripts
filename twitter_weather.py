import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as md
from TwitterAPI import TwitterAPI

glasgow = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=2648579&units=metric&APPID=25041c56770cfc0cdb9edbf6371bc2d4")
glasgow.raise_for_status()
glasgow_json = json.loads(glasgow.text)

df = pd.DataFrame(glasgow_json['list'])
df = df[['main','dt']]
df = df.rename(columns={'main': 'Temp', 'dt': 'Date \ Time'})
df['Temp'] = [df['Temp'][index]['temp'] for index, line in enumerate(df['Temp'])]
df['Date \ Time'] = [datetime.datetime.fromtimestamp(value) for value in df['Date \ Time']]


ax=plt.gca()
xfmt = md.DateFormatter('%Y-%m-%d %H:%Mam')
ax.xaxis.set_major_formatter(xfmt)
plt.plot(df['Date \ Time'],df['Temp'], 'k--^')
plt.xticks(rotation=10)
plt.grid(axis='both',color='r')
plt.ylabel("Temp (DegC)")
plt.ylim(min(df['Temp'])-1,max(df['Temp'])+1)
plt.title("Forecast Temperature Glasgow")
plt.savefig('five_day_forecast_glasgow.png',dpi=300)


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
file = open('five_day_forecast_glasgow.png', 'rb')
data = file.read()
r = api.request('statuses/update_with_media', {'status':'5 Day Forecast for Glasgow from {} to {}'.format(df['Date \ Time'][0], df['Date \ Time'][len(df['Date \ Time'])-1])}, {'media[]':data})
print(r.status_code)