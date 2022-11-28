import requests
import json
from bs4 import BeautifulSoup
import csv
import datetime
import time

##TOKEN = 20aaada9ceb74fa4aff1429185f1b37d

def GetUnixTime(time):
    time_object = datetime.datetime.strptime(time, "%a, %d %b %Y %H:%M:%S %z")
    print(time_object)
    unix_time = time_object.timestamp()
    print(unix_time)
    return unix_time

###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################

my_headers = {'accept' : 'application/json'}

duplicateNews = [10]
last_time = None

with open('historical_headlines_benzinga.csv', 'r', newline = '', encoding = "utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',',  quoting = csv.QUOTE_MINIMAL)
    for row in reader:
        news_id_load = row[0]
        news_id_load = int(news_id_load)
        duplicateNews.append(news_id_load)

        last_time = row[1]


if last_time is not None:
    unixTime = GetUnixTime(last_time)
else:
    unixTime = 1609477200.0

unixTime = str(unixTime)
unixTime = unixTime[:-2]
unixTime = int(unixTime)
unixTime = unixTime - 3900

with open('historical_headlines_benzinga.csv', 'a', newline = '', encoding = "utf8") as csvfile2:
    writer = csv.writer(csvfile2, delimiter = ',',  quoting = csv.QUOTE_MINIMAL)

    while unixTime < 1654660772:
        start_time=time.time()

        get_url = f"https://api.benzinga.com/api/v2/news?pageSize=10000&displayOutput=full&publishedSince={unixTime}&sort=created%3Aasc&token=20aaada9ceb74fa4aff1429185f1b37d"

        response = requests.get(get_url, headers=my_headers)

        i = 0
        while i < len(response.json()):
            jsonResp = json.dumps(response.json()[i])
            jsonLoad = json.loads(jsonResp)

            news_body_html = jsonLoad['body']
            body_soup = BeautifulSoup(news_body_html, 'html.parser')
            newsBody = body_soup.get_text()
            newsBody = newsBody.replace(",", " ")
            newsBody = "\" " + newsBody + " \""
            newsBody = "\" " + newsBody + " \""
            newsBody = "\" " + newsBody + " \""

            newsAuthor = jsonLoad['author']
            newsDate = jsonLoad['created']
            newsHeadline = jsonLoad['title']
            newsURL = jsonLoad['url']
            newsID = jsonLoad['id']
            newsStocks = jsonLoad['stocks']
            newsStocks = str(newsStocks)

            newsInfo = [newsID, newsDate, newsAuthor, newsURL, newsStocks, newsHeadline, [newsBody]]

            if newsID not in duplicateNews:
                writer.writerow(newsInfo)
                print(newsDate)

            duplicateNews.append(newsID)
            i+=1

        display_time = datetime.datetime.fromtimestamp(unixTime)
        print(display_time) 
        unixTime += 30
        programTime = round(time.time() - start_time, 2)
        print("\n--- %s seconds --- \n" % (programTime))