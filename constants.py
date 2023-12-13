# data file - hardcoded for now
# DATA_FILE = 'data/prompts_centene_short.csv'
# DATA_FILE = 'data/centene_test_set.csv'
# DATA_FILE = 'data/centene_test_set_1.csv'
DATA_FILE = 'data/centene_test_set_2.csv'

# classifications
CLASSIFICATIONS = ['Authorizations', 'Benefits', 'Billing', 'ChangeAddress', 'ChangeProvider', 
                   'DentalCoverage', 'Eligibility', 'FallbackIntent', 
                   'FindProvider', 'MedicareForms', 'OTCQuestions',
                   'PharmacyLocation', 'PharmacyMedication', 'PlaceOTCOrder', 'RequestIDCard', 
                   'RequestTransportation']


# AWS creds
AWS_PROFILE_NAME = '135899518107_AdministratorAccess'
AWS_REGION_NAME = 'us-east-1'

# Framework selections (OpenAI or Bedrock)
FRAMEWORK_OPENAI = 'OpenAI'
FRAMEWORK_BEDROCK = 'AWS Bedrock'

# Model selections
MODEL_OPENAI_GPT_3_5_TURBO = 'gpt-3.5-turbo'
MODEL_BEDROCK_TITAN_LITE_V1 = 'amazon.titan-text-lite-v1'
MODEL_BEDROCK_COHERE_V14 = 'cohere.command-text-v14'
MODEL_BEDROCK_JURASSIC2_MID_V1 = 'ai21.j2-mid-v1'
MODEL_BEDROCK_JURASSIC2_ULTRA_V1 = 'ai21.j2-ultra-v1'
MODEL_BEDROCK_LLAMA2_70B_CHAT_V1 = 'meta.llama2-70b-chat-v1'

# Heatmap for comparison evaluation
HEATMAP_FONT_SIZE = 3

