from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def emotionDetector():
    # Get the input text from the JSON body of the request
    data = request.get_json()
    text_to_analyze = data.get("text")
    
    # Check if the text was provided
    if not text_to_analyze:
        return jsonify({"error": "No text provided for analysis"}), 400

    # Call the emotion_detector function and get the response
    try:
        emotion_result = emotion_detector(text_to_analyze)
        return jsonify({"emotion_analysis": emotion_result})
    except Exception as e:
        # Handle errors and return an error message with a 500 status code
        return jsonify({"error": str(e)}), 500
