from flask import Flask


app = Flask(__name__)

@app.route("/")
def root():
    return {
        "content_type": 'Content-Type: text/plain',
        "content": 'Hello there Martin from App Engine.'
    }

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
