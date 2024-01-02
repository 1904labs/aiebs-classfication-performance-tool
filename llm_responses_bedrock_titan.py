import json


def get_classification_results(prompt, model_selection, client):
    # response
    body = json.dumps({
        'inputText': prompt,
        'textGenerationConfig': {
            'maxTokenCount': 4096,
            'stopSequences': [],
            'temperature': 0,
            'topP': 1
        }
    })
    kwargs = {
        'body': body,
        'modelId': model_selection,
        'accept': 'application/json',
        'contentType': 'application/json'
    }    
    response = client.invoke_model(**kwargs)

    # parse response
    response_body = json.loads(response.get('body').read())
    result = response_body['results'][0]['outputText']

    return result
