"""
Description:
    The main process for the NHL twitter bot application.
"""

import threading
from flask import Flask
from os import path

from src import bot

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """
    Front-end of the web application.
    """
    if not path.exists ("bot.log"):
        return ""

    with open("bot.log", encoding="utf-8") as log_file:
        return log_file.read()

if __name__ == '__main__':

    # Run the twitter bot in the background
    bot_thread = threading.Thread (target = bot.check_for_updates, daemon = True)
    bot_thread.start()

    # Run the front-end web application
    app.run(host="0.0.0.0", port=5000, threaded=True)
