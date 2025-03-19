from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()
from langchain_anthropic import ChatAnthropic
# llm = ChatOllama(model='llama3.2')
llm = ChatAnthropic(model='claude-3-7-sonnet-20250219')

prompt = '''
Given a list of features: {list_of_features}, create a single feature that combines the two to three most relevant features from the list.
Requirements:
The feature should be described as a one-page mobile webpage.
The design must follow a scrollable interaction model, avoiding tabbed navigation. The content should flow naturally in a continuous vertical scroll for a seamless user experience.
'''

StrParser = StrOutputParser()

CombinedFeaturePrompt = PromptTemplate(template=prompt,input_variables=['list_of_features'])

CombinedFeatureProcess = CombinedFeaturePrompt|llm|StrParser
