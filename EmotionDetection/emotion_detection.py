import requests
import json

def emotion_detector(text_to_analyze):
    """
    Processes a text string with Watson NLP Emotion Predict service
    and returns a structured dictionary containing individual emotion 
    scores and the dominant emotion.
    """
    # Target endpoint URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Required metadata identification headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Request JSON payload structural schema
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Execute the POST request
    response = requests.post(url, json=myobj, headers=headers)
    
    # Convert response text into a dictionary using the json library
    formatted_response = json.loads(response.text)
    
    # Extract the dictionary containing the emotions and their scores
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extract individual emotion scores
    anger_score = emotion_scores['anger']
    disgust_score = emotion_scores['disgust']
    fear_score = emotion_scores['fear']
    joy_score = emotion_scores['joy']
    sadness_score = emotion_scores['sadness']
    
    # Write code logic to find the dominant emotion (highest score)
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Construct the formatted output dictionary structure
    output_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return output_dict