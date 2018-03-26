from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.shortcuts import render


def chat(request):
    context = {}
    return render(request, 'chatbot/chatbot.html', context)


# def respond_to_websockets(message):
#     import requests
#     app_client_id = `00f02700-7b90-4adc-88d5-0762b0e5b734`
#     app_client_secret = `kmumbP12kwEVCQAG160)]_{`
#     def sendMessage(serviceUrl,channelId,replyToId,fromData, recipientData,message,messageType,conversation):
#         url="https://login.microsoftonline.com/common/oauth2/v2.0/token"
#         data = {"grant_type":"client_credentials",
#             "client_id":app_client_id,
#             "client_secret":app_client_secret,
#             "scope":"https://graph.microsoft.com/.default"
#            }
#         response = requests.post(url,data)
#         resData = response.json()
#         responseURL = serviceUrl + "v3/conversations/%s/activities/%s" % (conversation["id"],replyToId)
#         chatresponse = requests.post(
#                            responseURL,
#                            json={
#                             "type": messageType,
#                             "timestamp": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%zZ"),
#                             "from": fromData,
#                             "conversation": conversation,
#                             "recipient": recipientData,
#                             "text": message,
#                             "replyToId": replyToId
#                            },
#                            headers={
#                                "Authorization":"%s %s" % (resData["token_type"],resData["access_token"])
#                            }
#                         )


def respond_to_websockets(message):
    jokes = {
     'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
     'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
     'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
     }  

    result_message = {
        'type': 'text'
    }
    if 'fat' in message['text']:
        result_message['text'] = random.choice(jokes['fat'])
    
    elif 'stupid' in message['text']:
        result_message['text'] = random.choice(jokes['stupid'])
    
    elif 'dumb' in message['text']:
        result_message['text'] = random.choice(jokes['dumb'])

    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message['text'] = "Hello to you too! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."
    else:
        result_message['text'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, stupid or dumb."

    return result_message
