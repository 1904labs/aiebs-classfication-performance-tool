import pandas as pd
from constants import *


def get_prompt():
    df = pd.read_csv(DATA_FILE)
    user_utterances_block  = '\n'.join([f'{i + 1}. {user_utterance}' for i, user_utterance in enumerate(list(df.utterances))])
    prompt = f'''
    Roleplay: You are a customer service dispatcher at a a medical benefits brokerage company.

    Task: Identify (and only identify) the intent of a user request.

    Guidelines:
    - Classify each item of the numbered list appearing in triple backticks into one of the following categories.
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
    ```
    1. "I haven't received my ID card yet, what should I do?"
    2. "What's the process for buying OTC vitamins through my plan?"
    3. "Can I get reimbursed for travel expenses to medical facilities?"
    4. "I need a copy of my last billing statement."
    5. "Are orthodontic services included in my dental plan?"
    6. "Can you help me understand the eligibility criteria for maternity benefits?"
    7. "Can I transfer to a different dentist under my plan?"
    8. "I need to purchase a new thermometer, how can I do that?"
    9. "Is there a brochure available on Medicare Advantage plans?"
    10. "How do I update my billing information?"
    11. "What's the copay for a dental cleaning?"
    12. "Is there a copay for over-the-counter medications?"
    13. "Can you recommend a good OTC remedy for a sore throat and some first aid supplies?"
    14. "How do I find a healthcare provider for a specific treatment?"
    15. "What are the guidelines for using the transport benefit?"
    16. "I need to purchase a pain relief cream and some multivitamins."
    17. "Who should I inform about my relocation for insurance purposes?"
    18. "How long does it take to receive authorization for tests?"
    19. "Can you help me order a glucose monitoring kit?"
    20. "What do I need to do to start seeing a new therapist?"
    21. "What wellness programs does my plan offer?"
    22. "How can I ensure all my insurance documents come to my new home?"
    23. "Where can I find details about Medicare prescription coverage?"
    24. "Can you explain my prescription coverage?"
    25. "Am I covered for emergency room visits?"
    26. "Is pre-authorization required for my new medication?"
    27. "Is a referral required for specialist consultations?"
    28. "What is the process to add a new dependent to my policy?"
    29. "Which pharmacies can I use for prescription delivery?"
    30. "Can you send me a temporary ID card while I wait for the original?"
    31. "I need to locate a physical therapist covered by my plan."
    32. "Is there a preferred pharmacy for my medications?"
    ```

    Answers:
    1. RequestIDCard
    2. OTCQuestions
    3. RequestTransportation
    4. Billing
    5. DentalCoverage
    6. Eligibility
    7. ChangeProvider
    8. OTCQuestions
    9. MedicareForms
    10. Billing
    11. DentalCoverage
    12. OTCQuestions
    13. PlaceOTCOrder
    14. FindProvider
    15. RequestTransportation
    16. PlaceOTCOrder
    17. ChangeAddress
    18. Authorizations
    19. OTCQuestions
    20. ChangeProvider
    21. Benefits
    22. ChangeAddress
    23. MedicareForms
    24. PharmacyMedication
    25. Benefits
    26. PharmacyMedication
    27. Authorizations
    28. Eligibility
    29. PharmacyLocation
    30. RequestIDCard
    31. FindProvider
    32. PharmacyLocation

    Roleplay: You are a customer service dispatcher at a a medical benefits brokerage company.

    Task: Identify (and only identify) the intent of a user request.

    Guidelines:
    - Classify each item of the numbered list appearing in triple backticks into one of the following categories.
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
    ```
    {user_utterances_block}
    ```

    Answers:

    '''
    
    return prompt
