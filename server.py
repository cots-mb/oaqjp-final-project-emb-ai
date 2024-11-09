"""
Flask application to analyze emotions in text using Watson NLP's Emotion Detection API.
"""
from flask import Flask, request, jsonify, render_template
# Import the emotion detection function from Emotion Detection module
from EmotionDetection.emotion_detection import emotion_detector
#initating flask app
app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Endpoint to load index.html.

    Returns:
        Returns the start side of the application
    """
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector():
    """
    Endpoint to analyze the emotions in provided text.

    This route accepts a GET request with a JSON payload containing a 'text' field.
    It uses the `emotion_detector` function to analyze the text's emotional content
    and returns the results in JSON format.

    Returns:
        JSON response: A JSON object with the analyzed emotional content of the text,
        or an error message if input is invalid or an internal error occurs.
    """
    #myStatus to store the API status
    my_status = 0
    # Get the input text from the request
    text_to_analyze = request.args.get("textToAnalyze")
    # Check if the text was provided
    #if not text_to_analyze:
    #    return jsonify({"message": "No text provided for analysis"}), 422
    try:
        # Call the emotion_detector function and analyze the text
        emotion_result = emotion_detector(text_to_analyze)
        #Check API Status to handel 400 error
        if emotion_result == 'Error':
            emotion_result = [{'anger': None, 'disgust': None,
            'fear': None, 'joy': None, 'sadness': None}]
            message = "Invalid text! Please try again!"
            my_status = 400
        else:
            my_status = 200
            message = "For the given statement, the system response is "
    except ImportError as error:
        # Handle errors and return an error message with a 500 status code
        return jsonify({"error": str(error)}), 500
    # Return the analysis result in JSON format
    return jsonify({message: emotion_result}),my_status
