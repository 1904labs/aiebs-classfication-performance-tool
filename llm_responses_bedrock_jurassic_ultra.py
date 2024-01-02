import json


def get_classification_results(prompt, model_selection, client):
    # response
    body = json.dumps({
        'prompt': prompt,
        'maxTokens': 500,
        'temperature': 0,
        'topP': 1,
        # 'stop_sequences': [],
        # 'countPenalty': {'scale': 0},
        # 'presencePenalty': {'scale': 0},
        # 'frequencyPenalty': {'scale': 0}  
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
    result = response_body['completions'][0]['data']['text']

    return result
