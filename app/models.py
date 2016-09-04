# coding:utf-8
import requests


class days():
    pic_map = {u'晴': 'weather/3.png',
               u'沙尘暴': 'weather/4.png', u'浮尘': 'weather/4.png', u'扬沙': 'weather/4.png',
               u'雾': 'weather/5.png', u'霾': 'weather/.png', u'强沙尘暴': 'weather/.png',
               u'多云': 'weather/6.png',
               u'阴': 'weather/7.png',
               u'阵雨': 'weather/9.png',
               u'雷阵雨': 'weather/10.png',
               u'小雨': 'weather/11.png',
               u'中雨': 'weather/12.png', u'大雨': 'weather/12.png', u'小雨转中雨': 'weather/12.png', u'中雨转大雨': 'weather/12.png',
               u'雷阵雨伴有冰雹': 'weather/13.png',
               u'暴雨': 'weather/14.png', u'大暴雨': 'weather/14.png', u'特大暴雨': 'weather/14.png', u'大雨转暴雨': 'weather/14.png',
               u'暴雨转大暴雨': 'weather/14.png', u'大暴雨转特大暴雨': 'weather/14.png',
               u'雨夹雪': 'weather/15.png',
               u'阵雪': 'weather/16.png', u'小雪': 'weather/16.png',
               u'中雪': 'weather/17.png', u'小雪转中雪': 'weather/17.png',
               u'大雪': 'weather/18.png', u'暴雪': 'weather/18.png', u'中雪转大雪': 'weather/18.png', u'大雪转暴雪': 'weather/18.png',
               u'冻雨': 'weather/19.png',
               u'': ''
               }

    def __init__(self, date, weather, wind, temperature):
        self.date = date
        self.weather = weather
        # self.pic = self.get_pic(weather)
        self.wind = wind
        self.temperature = temperature

        self.weather_split(weather)
        self.get_pic(self.l_weather, self.r_weather)

    def weather_split(self, weather):
        zhuan = u'转'
        zhuan_index = weather.find(zhuan)
        if zhuan_index != -1:
            self.l_weather = weather[:zhuan_index]
            self.r_weather = weather[zhuan_index + 1:]
        else:
            self.l_weather = weather
            self.r_weather = weather

    def get_pic(self, l_weather, r_weather):
        self.l_pic_url = days.pic_map[l_weather]
        self.r_pic_url = days.pic_map[r_weather]

    @classmethod
    def weather(cls, city,ists_list):
        payload = {'location': city, 'output': 'json', 'ak': 'djYMsCshZb4UGzA55TsaeGpEWP3denxx'}
        r = requests.get("http://api.map.baidu.com/telematics/v3/weather", params=payload)
        if r.json()['status']=='success':
            weather_dict = r.json()['results'][0]['weather_data']
        else:
            return False
        for item in weather_dict:
            ists = days(item['date'], item['weather'],
                        item['wind'], item['temperature'])
            ists_list.append(ists)
        return True
