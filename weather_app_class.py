import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime
from TwitterAPI import TwitterAPI

class weather_temp():
    '''
    Weather_location = weather_temp(location, consumer_key, consumer_secret, access_token_key, access_token_secret, location_id, api_id, num_of_days=5)

    location is just the name of the area you are tweeting about, although it is only for printing the name on the tweets but does not help with location data
    consumer and access token info is acquired from your twitter account
    location_id needs to be found from the http://openweathermap.org/help/city_list.txt by search for your location and taking the info from the id column
    api_id is required to take the information from http://openweathermap.org/, this is found by creating an account and finding your profiles api id
    number of days is how many days you wish to show not including today, it defaults to 5 days so it would mean you see 5 days in the future minus today
    '''


    def __init__(self,location, consumer_key, consumer_secret, access_token_key, access_token_secret, location_id, api_id, num_of_days=4):
        self.api_id = api_id
        self.location = location
        self.location_id = location_id
        self.consumer_key =consumer_key
        self.consumer_secret = consumer_secret
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret
        self.num_of_days = num_of_days
        self.error_check = False

    def location_data(self):
        location_data = requests.get("http://api.openweathermap.org/data/2.5/forecast?id={}&units=metric&APPID={}".format(self.location_id, self.api_id))
        status_id = location_data.status_code
        if status_id != 200:
            print("Status code {} received, check details and try again.\n\nPROGRAM NOT RAN".format(status_id))
            return -1
        else:
            return json.loads(location_data.text)['list']

    def data_frame(self):
        temp_data = self.location_data()
        if temp_data == -1:
            self.error_check = True
        else:
            df = pd.DataFrame(temp_data)
            df = df[['main','dt']]
            df = df.rename(columns={'main': 'Temp', 'dt': 'UNIX Time'})
            df['Temp'] = [df['Temp'][index]['temp'] for index, line in enumerate(df['Temp'])]
            df['Time'] = [datetime.datetime.fromtimestamp(value) for value in df['UNIX Time']]
            self.df = df


    def date_range_for_graph(self):
        today = datetime.datetime.today().date()
        delta2 = datetime.timedelta(days=self.num_of_days)
        delta2_date = today + delta2
        time_mask = (self.df['Time'] >= today) & (self.df['Time'] <= delta2_date)
        self.df = self.df.loc[time_mask]

    def ploting_graph(self):
        ax=plt.gca()
        ax.xaxis.set_major_formatter(md.DateFormatter('%d/%m/%y %H:%M%p'))
        ax.xaxis.set_major_locator(md.HourLocator(byhour=[0]))
        ax.xaxis.set_minor_locator(md.HourLocator(byhour=[12]))
        plt.plot(self.df['Time'],self.df['Temp'], 'k--^')
        plt.xticks(rotation=0)
        plt.grid(axis='both',color='r')
        plt.ylabel("Temp (DegC)")
        plt.xlim(min(self.df['Time']-datetime.timedelta(hours=2)),max(self.df['Time']+datetime.timedelta(hours=2)))
        plt.ylim(min(self.df['Temp'])-1,max(self.df['Temp'])+1)
        plt.title("Forecast Temperature {}".format(self.location))
        plt.savefig('{}_day_forecast_{}.png'.format(self.num_of_days,self.location),dpi=300)

    def tweet_graph(self):
        api = TwitterAPI(self.consumer_key, self.consumer_secret, self.access_token_key, self.access_token_secret)
        file = open('{}_day_forecast_{}.png'.format(self.num_of_days,self.location), 'rb')
        data = file.read()
        r = api.request('statuses/update_with_media', {
            'status': '{0} Day Temperature Forecast for {1} from {2} to {3} #{1}'.format((self.num_of_days-1), self.location, self.df.iloc[0]['Time'],
                                                                                             self.df.iloc[-1]['Time'])},
                        {'media[]': data})
        print(r.status_code)

    def start_tweeting(self):
        self.data_frame()
        if self.error_check == False:
            self.date_range_for_graph()
            self.ploting_graph()
            self.tweet_graph()
            print("Program Completed")
        else:
            print("INFORMATION INCORRECT")

# Weather_location = weather_temp(location, consumer_key, consumer_secret, access_token_key, access_token_secret, location_id, api_id, num_of_days=5)
Weather_location = weather_temp()
Weather_location.start_tweeting()


