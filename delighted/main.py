from flask import Flask, request
import os
import logging


app = Flask(__name__)

DB_PATH = os.path.join('data', 'customer_data.db')


# Error handling new code
@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500



@app.route('/')
def hello_world():
    return 'Hello, Hossain Ahmed!'



if __name__ == '__main__':
    app.run(debug=True)


