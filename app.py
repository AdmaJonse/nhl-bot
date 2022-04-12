import os

from datetime import datetime
from flask import Flask, render_template
from multiprocessing import Process
from src import bot
from src import logger
from time import sleep


app = Flask(__name__, static_folder="app/static/", template_folder="app/static/")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stream')
def stream():
    def generate():
        with open('job.log', 'r') as f:
            while True:
                yield f.read()
                sleep(1)

    return app.response_class(generate(), mimetype='text/plain')


if __name__ == "__main__":
    
    open('job.log', 'w').close()

    Process(target=bot.check_for_updates).start()

    logger.log_info("Application deployed at: " + str(datetime.now()))
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, threaded=True)