from constants import *
import pandas as pd
import re

def parse_intent(message):
    try:
        # delete any text before numbered list
        start = message.find('1. ')
        s = message[start:]

        # parse each item of numbered list into a list
        pattern = r'[0-9]+. '
        lines = re.split(pattern, s)[1:]  # delete '' at index 0

        # find classifications for each item of numbered list
        result = []
        for i, line in enumerate(lines):
            is_found = False
            for classification in CLASSIFICATIONS:
                if classification.lower() in line.lower():
                    result.append(classification)
                    is_found = True
                    break  # if multiple classfications, grab first one
            if not is_found:
                result.append('unknown')
    except:
        result = ['unknown']    

    return result


def parse_message_content(DATA_FILE, message):
    '''
    Parse the message content into a list of (predicted intent: xx, actual_intent: xx,user_utterance: xx) dicts.
    '''
    df = pd.read_csv(DATA_FILE)
    predicted_intents = parse_intent(message)
    user_intents = list(df.intents)
    user_utterances = list(df.utterances)

    content = [{'predicted_intent': predicted_intent,
                'actual_intent': user_intents[i],
                'user_utterance': user_utterances[i]
                }
                for i, predicted_intent in enumerate(predicted_intents)]

    return content
