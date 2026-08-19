import requests, json
def sentiment_analyzer(text_to_analyze):  # Define function that takes str input
    '''function to run sentiment detection'''
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = {"raw_document":{"text":text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"} # Set the headers required for the API request 
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers 
    formatted_response = json.loads(response.text) # Return the response text from the API
    if 'documentSentiment' in formatted_response:
        sentiment = formatted_response['documentSentiment']
        label = sentiment['label']
        score = sentiment['score']
        return {'label': label, 'score': score}
    return {'label': None, 'score': None}
