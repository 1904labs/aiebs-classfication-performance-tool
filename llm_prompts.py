from constants import *
import llm_prompts_openai, llm_prompts_bedrock_cohere, llm_prompts_bedrock_jurassic_mid
import llm_prompts_bedrock_jurassic_ulta, llm_prompts_bedrock_titan, llm_prompts_bedrock_llama2


def prompt_dispatcher(framework_selection,
                      model_selection):
    '''
    Dispatches to the correct model function to give a response
    '''
    if framework_selection == FRAMEWORK_OPENAI:
        prompt = llm_prompts_openai.get_prompt()
    elif framework_selection == FRAMEWORK_BEDROCK:
        if model_selection == MODEL_BEDROCK_COHERE_V14:
            prompt = llm_prompts_bedrock_cohere.get_prompt()
        elif model_selection == MODEL_BEDROCK_JURASSIC2_MID_V1:
            prompt = llm_prompts_bedrock_jurassic_mid.get_prompt()
        elif model_selection == MODEL_BEDROCK_JURASSIC2_ULTRA_V1:
            prompt = llm_prompts_bedrock_jurassic_ulta.get_prompt()
        elif model_selection == MODEL_BEDROCK_TITAN_LITE_V1:
            prompt = llm_prompts_bedrock_titan.get_prompt()
        elif model_selection == MODEL_BEDROCK_LLAMA2_70B_CHAT_V1:
            prompt = llm_prompts_bedrock_llama2.get_prompt()
    return prompt