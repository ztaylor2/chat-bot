"""Bot responses."""
from microsoftbotframework import ReplyToActivity
import os

movie_subsription_key = os.environ.get('MOVIE_KEY')


def echo_response(message):
    """Respond to message."""
    if message["type"] == "message":
        cognitive_response = sentament_analysis(message)
        # import pdb; pdb.set_trace()
        user_intent = cognitive_response['intents'][0]['intent'].split('.')[1]
        ReplyToActivity(fill=message,
                        text=user_intent).send()


# def handle_response(message):
    """Handle messages sent from the user."""


def sentament_analysis(message):
    """Perform a sentament analysis on the text."""
    import requests

    try:
        res = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/c200592a-cb41-46de-8008-72f23c577591?subscription-key={}&verbose=true&timezoneOffset=0&q={}'.format(movie_subsription_key, message))
        return res.json()

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
