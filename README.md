# Benzinga-Historical-News
This program accesses and saves historical news events from Benzinga databases (Benzinga is a stock market news company). 

## Problem
We wanted to save large amounts of historical news events for use in backtesting and NLP model training from the Benzinga news databases. The goal of the program is to output a CSV with news events that include timestamp, ticker, headline, URL and news text body. 

## Solution and Process
This program is relatively simple, the process is visualized below:
![Blank diagram (3)](https://user-images.githubusercontent.com/118930217/204197533-6451227c-ba25-43eb-affa-18de017de43f.jpeg)

The program makes a connection to the Benzinga API. Once the request is made (only a limited number of news events can be pulled at once), the raw data is split up and added to the historical data CSV. After that news has been saved, the programs moves backwards in time for the next batch of news articles continuously until stopped. 

A sample of the output CSV is below:
![Screen Shot 2022-11-27 at 10 16 29 PM](https://user-images.githubusercontent.com/118930217/204199754-692a5d56-1fa5-457a-93e0-5eb86a55bd2c.jpg)

## Results Analysis
While working on NLP models or backtesting categories of news, it is useful to have large databases of news headlines, bodies, and events from which to pull. Our old database only had the ticker, datetime, and headline, and so this program created a better news database by saving more information. Ultimately the information saved helped to provide training data for NLP models, and backtesting examples on which to test. 

## Challenges
This program was not very challenging, however the limited batches did require some problem-solving so that the CSV would not contain duplicates.

## Other applications
N/A

## Potential Advancements
Overall this program would be significantly more useful if Benzinga did not limit the API calls to only a certain amount of news per batch. The most necesary advancement for this program would be to find a better source from which to pull for historical news. 
