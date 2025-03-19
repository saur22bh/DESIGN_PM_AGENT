from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()
from langchain_anthropic import ChatAnthropic
# llm = ChatOllama(model='llama3.2')
llm = ChatAnthropic(model='claude-3-7-sonnet-20250219')
prompt = '''
Given the following product feature name and its brief description, generate a detailed UI description for a mobile-native webpage that is entirely dedicated to showcasing this feature. The UI should be modern, visually appealing, and designed for an intuitive user experience.*  

 Feature Name : {FeatureName} 
 Feature Description : {feature}  

Key Requirements:   
1. Feature-Centric Design  – Since this page is exclusively for this feature, describe how it takes center stage. Will it be displayed in an interactive module, a full-screen showcase, a dynamic scrolling experience, or an immersive UI element?  
2. Visual Hierarchy & Emphasis  – How will the feature be highlighted? Will it have an eye-catching hero section, animated elements, or interactive demonstrations?  
3. Page Structure & Layout  – Define how the features applications will be shown on the webpage, ideally describing how this webpage would look like.  
4. Color Scheme & Styling  – Describe the modern design elements (e.g., soft gradients, glassmorphism, dark/light mode adaptability) that enhance the feature’s appearance.  
5. Typography & Icons  – Suggest font choices and iconography that fit the feature’s theme.  
6. User Flow & Interaction  – Explain how a user will engage with the feature on this dedicated page, from the first interaction to deeper engagement. 

Note :  [ Generate a detailed UI description for the main page of a product, assuming the user is already onboarded and actively using the service. 
Do not include any onboarding flows, welcome messages, or "get started" elements.
Example:
For a hydration tracker app, assume the user is logged in and already tracking their water intake. Focus on the UI elements that help the user log water, view progress, and track daily goals. Exclude any screens or components related to onboarding, tutorials, or initial setup.]


Note  : Make sure description is a string.
Output (Valid JSON)
{{
"Webpage_description" : "Description generated by LLM"
}}

'''

WebDescPromptTemplate = PromptTemplate(template=prompt,input_variables=['FeatureName','feature'])
parser = JsonOutputParser()
WebDescProcess = WebDescPromptTemplate|llm|parser

data = {'Smart Translator': {'rank': 1, 'mobile_usability': 9, 'engagement': 8, 'practicality': 8.5, 'total_score': 25.5, 'description': 'Real-time camera translation of signs, menus, and documents Offline language packs for common travel destinations Voice-to-voice translation for conversations with locals Phrasebook with common travel expressions organized by situation (restaurant, hotel, emergency)'}, 'Destination Language Prep': {'rank': 2, 'mobile_usability': 9, 'engagement': 8.5, 'practicality': 8, 'total_score': 25, 'description': 'Pre-trip language crash courses based on upcoming travel destinations Daily 5-minute language lessons tailored to planned activities Interactive pronunciation guide with feedback Cultural etiquette tips alongside language learning'}, 'Travel Itinerary Language Assistant': {'rank': 3, 'mobile_usability': 8.5, 'engagement': 7.5, 'practicality': 8, 'total_score': 24, 'description': "Scan and auto-translate booking confirmations and travel documents Suggest key phrases needed for each day's activities Emergency phrase generator with audio for urgent situations Location-based translation suggestions that change as you travel"}, 'Digital Travel Journal': {'rank': 4, 'mobile_usability': 9, 'engagement': 8, 'practicality': 8.5, 'total_score': 25.5, 'description': 'Document your travel with auto-translated local phrases and words Tag photos with local language descriptions Track language progress across different destinations Share multilingual travel stories with friends and community'}}
rank_1_entry = None
for key, value in data.items():
    if value['rank'] == 1:
        rank_1_entry = {key: value}
        break

feature_name = list(rank_1_entry.keys())[0]
desc = rank_1_entry[feature_name]['description']
# print(feature_name)
# print(desc)
# response = WebDescProcess.invoke({'FeatureName':feature_name,'feature':desc})
# print(response)