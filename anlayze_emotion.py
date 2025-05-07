import requests
import json
def emotion_detector(text_to_analyse):

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { 
        "raw_document": {
            "text": text_to_analyse } }

    response = requests.post(URL, headers=Headers, json=input_json)

    

    if response.status_code == 200:
        response_dict = json.loads(response.text)
        for emo in response_dict:
            print(emo)

        # Extract required emotions and their scores
        emotions ={
            'anger': response_dict['emotionPredictions'][0]['emotion']['anger'],
            'disgust': response_dict['emotionPredictions'][0]['emotion']['disgust'],
            'fear': response_dict['emotionPredictions'][0]['emotion']['fear'],
            'joy': response_dict['emotionPredictions'][0]['emotion']['joy'],
            'sadness': response_dict['emotionPredictions'][0]['emotion']['sadness']
        }
        

        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Add dominant_emotion to the emotions dictionary
        emotions['dominant_emotion'] = dominant_emotion

        return emotions
    else:
        print(f"Error: Unable to analyze emotion. Status code: {response.status_code}")

if __name__ == "__main__":
    text_to_analyze = "I love this new technology."
    result_text = emotion_detector(text_to_analyze)
    # res = json.dumps(result_text)
    print(result_text)
