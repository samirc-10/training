from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Define the API endpoint
@app.route('/hello', methods=['GET'])
def hello_world():
    """
    API endpoint to return a simple Hello World message.
    """
    return {"message": "Hello World"}, 200  # Return JSON response with status code 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode
