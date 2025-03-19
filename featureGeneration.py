from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate


from langchain_anthropic import ChatAnthropic

import os 
import streamlit as st
os.environ["ANTHROPIC_API_KEY"] = st.secrets["ANTHROPIC_API_KEY"]

llm = ChatAnthropic(model='claude-3-7-sonnet-20250219')

prompt = '''
You are a Product Manager designing a personalised native mobile webpage. Your goal is to maximize user engagement by generating highly relevant and interactive product features based on the given topic.
1. Interpret User Interests: - Process the given user interests: {user_interests} - Identify key themes from these interests to guide feature ideation. 
2. Generate Features: - Suggest interactive, mobile-friendly product features tailored to user_interests. - Ensure the features are practical and aligned with a native mobile experience. - Avoid generic or irrelevant features.
3. Output Format: - Provide a list of features with a brief description for each. In description include all required details about feature. Ensure clarity and usability in the feature names. 

'''


FeatureGenerationPromptTemplate = PromptTemplate(template=prompt,
                                                 input_variables=['user_interests']
                                                 )

parser = StrOutputParser()

FeatureGenerationProcess = FeatureGenerationPromptTemplate|llm|parser 



# response = FeatureGenerationProcess.invoke({'user_interests':'User is interested in travel and knows the importance of language translator while travelling'})
# print(response)
