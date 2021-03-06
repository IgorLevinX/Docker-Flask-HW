import os
from flask import Flask

app = Flask(__name__)
color = os.environ.get('APP_COLOR')
color = "green"

@app.route("/")
def main():
    return f'<html><body style="background:{color}"><h1><b>Welcome flask user!</b></h1></body></html>';

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)

