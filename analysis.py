from constants import *
import message_parsing

import numpy as np
import pandas as pd
import os
from datetime import datetime


def get_prediction_errors(message, data_file):
    try:
        prediction_errors = '<table><tr><th>Utterance</th><th>Predicted Intent</th><th>Actual Intent</th></tr>'
        results = message_parsing.parse_message_content(data_file, message)
        nbr_correct = 0
        error_nbr = 0
        for _, result in enumerate(results):
            if result['predicted_intent'].lower() == result['actual_intent'].lower():
                nbr_correct += 1
            else:
                error_nbr += 1
                prediction_errors += f"<tr><td>{result['user_utterance']}</td><td>{result['predicted_intent']}</td><td>{result['actual_intent']}</td></tr>"
                
        if nbr_correct > 0:
            prediction_percentage = 100 * nbr_correct / len(results)
        else:
            prediction_percentage = 0.
        prediction_errors += '</table><br>'

        nbr_total = nbr_correct + error_nbr
    
        return prediction_errors, nbr_correct, nbr_total, prediction_percentage
    except Exception as e:
        return np.nan, np.nan, np.nan, np.nan,


def get_logs_analysis_df(uploaded_files):
    dfs = []
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        timestamp = datetime.fromtimestamp(os.path.getctime('logs/' + uploaded_file.name))
        df['timestamp'] = timestamp
        dfs.append(df)
    logs_analysis_df = pd.concat(dfs, ignore_index=True)
    return logs_analysis_df


def analyze_df(logs_analysis_df):
    intents = ['billing', 'equipment_sales', 'subscriptions', 'subscription_cancellations', 
                  'tech_support_camera', 'tech_support_doorbell', 'tech_support_alarm', 'tech_support_other']

    bedrock_df = logs_analysis_df[logs_analysis_df.api==FRAMEWORK_BEDROCK]
    heatmap_bedrock_pred_intent = []
    heatmap_bedrock_accuracy = []
    for intent in intents:
        df = bedrock_df[bedrock_df.predicted_intent==intent]
        nbr_correct = df.is_correct.sum()
        nbr_total = len(df.index)
        percent_accuracy = int(100 * nbr_correct / nbr_total)

        heatmap_bedrock_pred_intent.append(intent)
        heatmap_bedrock_accuracy.append(percent_accuracy)
    heatmap_bedrock_df = pd.DataFrame({'predicted_intent': heatmap_bedrock_pred_intent, 'accuracy': heatmap_bedrock_accuracy})
    heatmap_bedrock_df['api'] = 'Bedrock'

    openai_df = logs_analysis_df[logs_analysis_df.api==FRAMEWORK_OPENAI]
    heatmap_openai_pred_intent = []
    heatmap_openai_accuracy = []
    for intent in intents:
        df = openai_df[openai_df.predicted_intent==intent]
        nbr_correct = df.is_correct.sum()
        nbr_total = len(df.index)
        percent_accuracy = int(100 * nbr_correct / nbr_total)

        heatmap_openai_pred_intent.append(intent)
        heatmap_openai_accuracy.append(percent_accuracy)
    heatmap_openai_df = pd.DataFrame({'predicted_intent': heatmap_openai_pred_intent, 'accuracy': heatmap_openai_accuracy})
    heatmap_openai_df['api'] = FRAMEWORK_OPENAI

    # heatmap
    if (len(bedrock_df) > 0) and (len(openai_df) > 0):
        df = pd.concat([heatmap_bedrock_df, heatmap_openai_df]).reset_index(drop=True)
        heatmap_df = df.pivot(index='api', columns='predicted_intent', values='accuracy')
    elif (len(heatmap_bedrock_df) > 0):
        heatmap_df = heatmap_openai_df
    else:
        heatmap_df = heatmap_bedrock_df

    return heatmap_df, bedrock_df, openai_df
