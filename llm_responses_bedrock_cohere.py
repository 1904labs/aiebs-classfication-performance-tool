import json


def get_parsed_response(prompt, model_selection, client):
    # request
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
    
    # response
    response = client.invoke_model(**kwargs)
    
    # parse response
    response_body = json.loads(response.get('body').read())
    # response_text = response_body.get('generations')[0].get('text')
    result = response_body.get('generations')[0].get('text')

    # ## TODO: Proper formatting. This is hard-coded garbage.
    # ## hack to remove any junk at the end
    # ndx = response_text.find('71. ') + 4 # '71. '
    # ndx2 = response_text[ndx:].find('\n')
    # if ndx2 > 0:
    #     result = response_text[:ndx + ndx2].strip()
    # else:
    #     result = response_text.strip()

    return result
