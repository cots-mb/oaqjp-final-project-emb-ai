import requests

def emotion_detector(text_to_analyze):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    
    response = requests.post(url, headers=headers, json=payload)
    response = requests.post(url, headers=headers, json=payload)
    data = dict(json.loads(response.text))
    emo = dict(data["emotionPredictions"][0])
    
    if response.status_code == 200:
        
        return emo.get('emotion')

    else:
        
        return response.raise_for_status()
