import pandas as pd
from constants import *

def get_prompt():
    '''
    Assumes messages are in this order: system, assistant, user
    '''
    system_content = system_prompt_openai()
    assistant_content = assistant_prompt_openai()
    user_content = user_prompt_openai(DATA_FILE)

    messages = [
        {'role': 'system', 'content': system_content},
        {'role': 'assistant', 'content': assistant_content},
        {'role': 'user', 'content': user_content}
    ]
    return messages


def system_prompt_openai():
    content = '''
    You are a customer service dispatcher at a a medical benefits brokerage company.

    Task: Identify (and only identify) the intent of a user request.

    Guidelines:
    - Classify the text appearing in triple backticks into one of the following categories.
        - Authorizations
        - Benefits
        - Billing
        - ChangeProvider
        - ChangeAddress
        - DentalCoverage
        - Eligibility
        - FindProvider
        - MedicareForms
        - OTCQuestions
        - PharmacyLocation
        - PharmacyMedication
        - PlaceOTCOrder
        - RequestIDCard
        - RequestTransportation
    - For each item in the text in triple backticks, your reply will only be one of the single word classifications above. Do not include a period. Then please stop! Do not generate a further response. Do not ask for more information.
    - If there is no match for an item, please reply only with the single word "FallbackIntent". Then stop! Do not generate a further response. Do not ask for more information.
    - Be completely factual. Do not make anything up, even if the user asks you to.
    - Return the reply as a numbered list. Do not generate a response except for the numbered list. 
    
    Rigorous compliance to these instructions is imperative.
    ```{user_utterances_block}```   
    '''
    return content


def assistant_prompt_openai():
    content = '''
    Hello! Please describe your issue and I will classify your statement into the given categories.
    '''
    return content


def user_prompt_openai(data_file):
    '''
    Parses user content to a string
    '''
    df = pd.read_csv(data_file)
    user_content  = '\n'.join([f'{i + 1}. {user_utterance}' for i, user_utterance in enumerate(list(df.utterances))])
    return user_content
