# chat-bot
A chat bot built with Microsoft's Bot Framework, Language Understanding, and Text Analytics. 
Built on Flask with the Python package `microsoftbotframework 0.3.0`


## Getting started: 
- clone repository 
    - `https://github.com/ztaylor2/chat-bot.git`
- create python environment
    - `python3 -m venv ENV`
- add LUIS_KEY and TEXT_ANALYTICS_KEY to environment variables
    - `cd ENV/bin`
    - into the bottom of activate file, copy pasta:

        `export LUIS_KEY=<your_api_key>
        export TEXT_ANALYTICS_KEY=<your_api_key>`

- activate virtual environment
    - `source ENV/bin/activate`
- install dependencies 
    - `pip install -r requirements.txt`
- run server 
    - `python main.py`
