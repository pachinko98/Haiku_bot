import openai
import json
import requests
import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#News reporting API

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'category=technology&'
       'apiKey=API_KEY')

response = requests.get(url)
news_data = response.json()
description = news_data['articles'][0]['description'] if news_data['articles'][0]['description'] is not None else ''
title = news_data['articles'][0]['title'] if news_data['articles'][0]['title'] is not None else ''

#ChatGPT haiku maker
openai.api_key = 'API_KEY'
tprompt = 'make an eloquent haiku out of "' + description + ' ' + title + '"'
response = openai.Completion.create(
                            model="text-davinci-003",
                            prompt=tprompt,
                            max_tokens=30,
                            temperature=0.8)

text = str(response['choices'][0]['text'])

tweet = text.lstrip() + '\n' + news_data['articles'][0]['url']

print(tweet)

api.update_status(tweet)
