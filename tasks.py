"""Bot responses."""
from microsoftbotframework import ReplyToActivity, SendToConversation
import os
import requests

import urllib.parse
import urllib.error
import urllib.request
import json

luis_key = os.environ.get('LUIS_KEY')
text_analytics_key = os.environ.get('TEXT_ANALYTICS_KEY')


def init_conversation(message):
    """Begin conversation."""
    SendToConversation(fill=message,
                       conversationId='jg3alifjua8sdljn9abiuao4ihbimroivb',
                       text='Hi! I\'m a chat bot designed to help you find movies. Feel free to search for movies by actor, title, genre, or keyword.').send()


def handle_response(message):
    """Handle messages sent from the user."""
    if message["type"] == "message":
        cognitive_response = intention_analysis(message)
        response_text = generate_response(cognitive_response, message)

        sentiment = sentiment_analysis(message)

        print(sentiment)
        print(response_text)
        ReplyToActivity(fill=message,
                        text=response_text).send()


def intention_analysis(message):
    """Determine the intention of the user."""
    print(luis_key)
    try:
        res = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/c200592a-cb41-46de-8008-72f23c577591?subscription-key={}&q={}'.format(luis_key, message['text']))
        print(res)
        print(res.json())
        return res.json()

    except Exception as e:
        print(e)


def sentiment_analysis(message):
    """Determine the sentiment of the message."""
    sentiment_uri = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'

    headers = {
        'Ocp-Apim-Subscription-Key': text_analytics_key,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    sentiment_post_data = json.dumps({"documents": [{"id": "1", "language": 'en', "text": message['text']}]}).encode('utf-8')
    request = urllib.request.Request(sentiment_uri, sentiment_post_data, headers)
    response = urllib.request.urlopen(request)
    responsejson = json.loads(response.read().decode('utf-8'))
    sentiment = responsejson['documents'][0]['score']

    return sentiment


def generate_response(cognitive_response, message):
    """Generate the text response from the analysis from the language processing api."""
    # if no entity, default to title search
    if not cognitive_response['entities']:
        return 'Searching for {} in movie titles.'.format(message['text'])

    user_intent = cognitive_response['entities'][0]['type'].split('.')[1]
    entity = cognitive_response['entities'][0]['entity']
    if user_intent == 'Title':
        return 'Searching for movies with the title of {}.'.format(entity)
    elif user_intent == 'Person':
        return 'Searching for movies with {} as an actor.'.format(entity)
    elif user_intent == 'Keyword':
        return 'Searching for movies with keyword {}.'.format(entity)
    elif user_intent == 'Genre':
        return 'Searching for movies in the {} genre.'.format(entity)

    return 'gotta return something...'
