from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is running!"

if __name__ == '__main__':
    print("Starting Flask application...")  # Debugging output
    app.run(debug=True, host='localhost', port=5000)
