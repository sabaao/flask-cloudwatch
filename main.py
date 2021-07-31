import watchtower, flask, logging

logging.basicConfig(level=logging.INFO)
app = flask.Flask("loggable")
handler = watchtower.CloudWatchLogHandler()
app.logger.addHandler(handler)
logging.getLogger("werkzeug").addHandler(handler)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
