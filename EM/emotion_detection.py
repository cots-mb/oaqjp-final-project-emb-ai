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
     if response.status_code == 200:

        data = dict(json.loads(response.text))
        emoPre = dict(data["emotionPredictions"][0])
        emo= emoPre.get('emotion')
        dominant_emo =  max(emo, key=emo.get)
        emo['dominat_emotion'] = dominant_emo

        print("\n".join("{}\t{}".format(k, v) for k, v in emo.items()))
       
        #return emo

    else:
        
        return response.raise_for_status()
