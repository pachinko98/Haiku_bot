# Haiku_bot
twitter bot that posts haikus about current tech news

## How it works

This bot makes use of the following APIs to work:

Twitter API

OpenAI API

News API

1. It requests the headline, brief description, and article link of a current news article on tech from News API
2. A GPT-3 model uses the headline and description of the article to create a haiku
3. The script then posts the haiku with the link of the news article as a tweet. 

You can see the bot in action here: https://twitter.com/hAIku79343727
