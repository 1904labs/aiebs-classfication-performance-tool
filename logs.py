from constants import *
import message_parsing
import datetime as dt

import numpy as np

def make_log_report(data_file, message, api_selection, model_selection):
    # create log string
    ## TODO: 
    ## * predicted_intent_parsed is temp to see if the parsing routine works correctly.
    ## * When it works, replace predicted_intent with predicted_intent_parsed
    log_report = 'api,model,is_correct,actual_intent,predicted_intent,user_utterance,predicted_intent_parsed\n'
    results = message_parsing.parse_message_content(data_file, message) 
    for _, result in enumerate(results):
        log_report += f"{api_selection}," +\
                      f"{model_selection}," +\
                      f"{result['predicted_intent'] == result['actual_intent']}," +\
                      f"{result['predicted_intent']}," +\
                      f"{result['actual_intent']}," +\
                      f'\"{result["user_utterance"]}\"\n'

    # write log string to file
    date = dt.datetime.now()
    file_name = f'logs/{api_selection}_{model_selection}_{date:%Y-%m-%d_%H:%M:%S}.log'
    with open(file_name, 'a') as log_file:
        log_file.write(log_report)

    return file_name, log_report, date

def get_prediction_errors(log_file):
    prediction_error = 0
    nbr_correct = 0
    nbr_total = 0
    prediction_percentage = 0

    return prediction_error, nbr_correct, nbr_total, prediction_percentage

# def get_prediction_errors(message, data_file):
#     try:
#         prediction_errors = '<table><tr><th>Utterance</th><th>Predicted Intent</th><th>Actual Intent</th></tr>'
#         results = data_operations.parse_message_content(data_file, message)
#         nbr_correct = 0
#         error_nbr = 0
#         for _, result in enumerate(results):
#             if result['predicted_intent'].lower() == result['actual_intent'].lower():
#                 nbr_correct += 1
#             else:
#                 error_nbr += 1
#                 prediction_errors += f"<tr><td>{result['user_utterance']}</td><td>{result['predicted_intent']}</td><td>{result['actual_intent']}</td></tr>"
                
#         if nbr_correct > 0:
#             prediction_percentage = 100 * nbr_correct / len(results)
#         else:
#             prediction_percentage = 0.
#         prediction_errors += '</table><br>'

#         nbr_total = nbr_correct + error_nbr
    
#         return prediction_errors, nbr_correct, nbr_total, prediction_percentage
#     except Exception as e:
#         return np.nan, np.nan, np.nan, np.nan,
