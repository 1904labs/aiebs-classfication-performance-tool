import openai


def get_parsed_response(prompt, model_selection, openai_key):
    # creds
    openai.api_key = openai_key

    # get response
    response = openai.ChatCompletion.create(model=model_selection, messages=prompt)

    # parse response
    result = response.choices[0].message.content
    return result
