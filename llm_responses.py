from constants import *
import llm_responses_openai, llm_responses_bedrock_cohere, llm_responses_bedrock_titan
import llm_responses_bedrock_jurassic_mid, llm_responses_bedrock_jurassic_ultra, llm_responses_bedrock_llama2


def response_dispatcher(prompt,
                        framework_selection,
                        model_selection,
                        openai_key=None,
                        aws_client=None):
    '''
    Dispatches to the correct model function to give a response
    '''
    if framework_selection == FRAMEWORK_OPENAI:
        response = llm_responses_openai.get_classification_results(prompt, model_selection, openai_key)
    elif framework_selection == FRAMEWORK_BEDROCK:
        if model_selection == MODEL_BEDROCK_COHERE_V14:
            response = llm_responses_bedrock_cohere.get_classification_results(prompt, model_selection, aws_client)
        elif model_selection == MODEL_BEDROCK_JURASSIC2_MID_V1:
            response = llm_responses_bedrock_jurassic_mid.get_classification_results(prompt, model_selection, aws_client)
        elif model_selection == MODEL_BEDROCK_JURASSIC2_ULTRA_V1:
            response = llm_responses_bedrock_jurassic_ultra.get_classification_results(prompt, model_selection, aws_client)
        elif model_selection == MODEL_BEDROCK_TITAN_LITE_V1:
            response = llm_responses_bedrock_titan.get_classification_results(prompt, model_selection, aws_client)
        elif model_selection == MODEL_BEDROCK_LLAMA2_70B_CHAT_V1:
            response = llm_responses_bedrock_llama2.get_classification_results(prompt, model_selection, aws_client)

    return response
