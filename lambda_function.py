from requests import get
from bs4 import BeautifulSoup
import re
from twilio.rest import Client
import os

def lambda_handler(event, context):

    # grab html of sydney BOM page
    url = "http://www.bom.gov.au/nsw/forecasts/sydney.shtml"
    html = get(url)
    bs = BeautifulSoup(html.text, "html.parser")

    # scrap relevant weather info
    forecast_date = bs.find("p", attrs={"class": "date"}).text.rstrip('.').replace(" at", "").replace(" on", ",")
    max_temp = bs.find("em", attrs={"class": "max"}).text
    weather_summary = bs.find("dd", attrs={"class": "summary"}).text.rstrip('.')
    rain_chance = bs.find("em", attrs={"class": "pop"}).text.rstrip('\t\n')
    alerts = bs.find("div", attrs={"class": "day main"}).find_all("p", attrs={"class": "alert"})

    # extract sun protection info from list of alerts
    for alert in alerts:
        if re.search('(Sun protection)(.+?)', alert.text):
            uv_summary = alert.text.replace("  ", " ")
            break
    
    # extract times of UV protection if stated
    uv_re = re.search('(from )(.+?)( to )(.+?)(,)', uv_summary)
    if uv_re:
        uv_times = "{} to {}".format(uv_re.group(2), uv_re.group(4))
    else:
        uv_times = "Not needed"

    # compose text message
    msg = "*Sydney Weather Today*\n({})\nMax Temp: {}\nWeather: {}\nRain: {}\nSun Protection: {}".format(forecast_date, max_temp, weather_summary, rain_chance, uv_times)

    # send sms message using twilio
    client = Client(os.environ.get("account_sid"), os.environ.get("auth_token"))
    client.messages.create(body=msg, from_=os.environ.get("from_number"), to=os.environ.get("to_number"))