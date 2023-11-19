import os
from flask import Flask, request

max_storage_mb = int(os.getenv('MAX_STORAGE_MB'))
directory_path = os.getenv('DIRECTORY_PATH')

app = Flask(__name__)

@app.route('/')
def home():
    """
    Home route that returns a welcome message.
    
    Returns:
        str: A welcome message.
    """
    return 'Welcome to MetricsLocal!'

@app.route('/i', methods=['GET'])
def process_request():
    """
    Processes incoming GET requests by extracting query parameters.
    
    Returns:
        dict: A dictionary containing the query parameters.
        int: HTTP status code.
    """
    query_params = {
        "app_key": request.args.get("app_key"),
        "timestamp": request.args.get("timestamp"),
        "hour": request.args.get("hour"),
        "dow": request.args.get("dow"),
        "tz": request.args.get("tz"),
        "sdk_version": request.args.get("sdk_version"),
        "sdk_name": request.args.get("sdk_name"),
        "user_details": request.args.get("user_details"),
        "device_id": request.args.get("device_id"),
        "checksum": request.args.get("checksum")
    }

    # TODO: Validate the checksum
    # TODO: Store the data in a file

    # Return a response (for now, just echoing the received parameters)
    return query_params, 200

if __name__ == '__main__':
    """
    Main entry point of the application when run as a standalone script.
    Starts a Flask server on host 0.0.0.0 and port 80.
    """
    app.run(host='0.0.0.0', port=80)