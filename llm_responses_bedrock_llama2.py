import json


def get_parsed_response(prompt, model_selection, client):
    # request
    body = json.dumps({
            "prompt": prompt,
            # "max_gen_len": 512,
            "temperature": 0,
            "top_p": 1
    })
    kwargs = {
        'body': body,
        'modelId': model_selection,
        'accept': 'application/json',
        'contentType': 'application/json'
    }
    
    # response
    response = client.invoke_model(**kwargs)

    # parse response
    response_body = json.loads(response.get('body').read())
    result = response_body ['generation']

    return result
