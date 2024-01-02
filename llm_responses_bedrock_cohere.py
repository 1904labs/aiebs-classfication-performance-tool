import json


def get_classification_results(prompt, model_selection, client):
    # response
    body = json.dumps({
        'prompt': prompt, 
        'max_tokens': 500,
        'temperature': 0
    })  
    kwargs = {
        'body': body,
        'modelId': model_selection,
        'accept': '*/*',
        'contentType': 'application/json'
    }    
    response = client.invoke_model(**kwargs)
    
    # parse response
    response_body = json.loads(response.get('body').read())
    result = response_body.get('generations')[0].get('text')

    return result
