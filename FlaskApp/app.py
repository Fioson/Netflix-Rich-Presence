from flask import Flask, request, jsonify
from flask_cors import CORS
import pypresence
import logging
import os
p = pypresence.Presence('YOUR DISCORD CLIENT ID HERE')
app = Flask(__name__)
cors = CORS(app)
log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True
p.connect()
os.system('cls')
try:
    @app.route('/send', methods=["GET", "POST"])
    def message():
        content = request.json
        if content["done"]:
            p.clear()
            return ""
        else:
            title = content['title']
            episode = content['name'] + " " + "(" + content['season'] + ")"
            url_episode = content['episode_url']
            p.update(state=episode, details=title, large_image="netflix", large_text="Netflix", buttons=[{"label": "Watch on Netflix", "url": url_episode}])
            os.system('cls')
            print("Updating:\nTitle: {}\nEpisode: {}\nTime Left: {}".format(title, episode, time_remaining))
            return ""

except KeyboardInterrupt:
    p.clear()
    p.close()
