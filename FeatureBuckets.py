from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


from langchain_anthropic import ChatAnthropic
import os 
import streamlit as st
os.environ["ANTHROPIC_API_KEY"] = st.secrets["ANTHROPIC_API_KEY"]

llm = ChatAnthropic(model='claude-3-5-sonnet-20241022')

prompt = '''
Compare the refined product features: {features} against the user interests: {user_interests}. Ensure that each feature is aligned with user needs and is well-suited for a mobile-first experience. Classify features as:
✅ Highly Relevant → Fully aligns with user needs.
⚠️ Somewhat Relevant → Useful but not directly requested.
❌ Irrelevant → Doesn’t fit user intent or mobile-native design.

Note : Feature descriptions are also given in inputs.
Note : Make sure the description returned for every feature is same as what was given in input for that feature.
Respond only in the following JSON format:
{{
  "Highly Relevant": [
    {{
      "feature_name": "Feature1",
      "description": "Detailed description of Feature1"
      "reason" : "Reason they were highly relevant"
    }},
    {{
      "feature_name": "Feature2",
      "description": "Detailed description of Feature2"
      "reason" : "Reason they were highly relevant"
    }}
  ],
  Somewhat relevant: [
    {{
      "feature_name": "FeatureX",
      "description": "Detailed description of FeatureX"
      "reason" : "Reason they were somewhat relevant"
     
    }},
    {{
      "feature_name": "FeatureY",
      "description": "Detailed description of FeatureY"
      "reason" : "Reason they were somewhat relevant"
    }}
  ],
  
  Not relevant: [
    {{
      "feature_name": "FeatureX",
      "description": "Detailed description of FeatureX"
      "reason" : "Reason they were not relevant"
     
    }},
    {{
      "feature_name": "FeatureY",
      "description": "Detailed description of FeatureY"
      "reason" : "Reason they were not relevant"
    }}
  ]
}}

'''
 









data_to_sent = '''
Features along with their descriptions : 
- Smart Translator: Real-time camera translation of signs, menus, and documents Offline language packs for common travel destinations Voice-to-voice translation for conversations with locals Phrasebook with common travel expressions organized by situation (restaurant, hotel, emergency)
- Destination Language Prep: Pre-trip language crash courses based on upcoming travel destinations Daily 5-minute language lessons tailored to planned activities Interactive pronunciation guide with feedback Cultural etiquette tips alongside language learning
- Travel Itinerary Language Assistant: Scan and auto-translate booking confirmations and travel documents Suggest key phrases needed for each day's activities Emergency phrase generator with audio for urgent situations Location-based translation suggestions that change as you travel
- Local Experience Finder: Discover authentic local experiences with language difficulty ratings Connect with language exchange partners at your destination Filter activities by language accessibility (English spoken, translation available, etc.) Community reviews from travelers with similar language backgrounds
- Cultural Context Companion: Learn cultural context alongside language (gestures, customs, taboos) AR overlay explaining cultural significance of landmarks and objects Local slang and idiom guide for each destination Region-specific etiquette tips to avoid cultural misunderstandings
- Digital Travel Journal: Document your travel with auto-translated local phrases and words Tag photos with local language descriptions Track language progress across different destinations Share multilingual travel stories with friends and community
- Global Payment Helper: Currency converter with visual price comparisons to home country Translated explanations of local payment systems and tipping customs Expense tracking with local and home currency Payment-related phrase guide for shopping and restaurants
'''




FeatureBucketPromptTemplate = PromptTemplate(template=prompt, input_variables=['features','user_interests'])
parser = JsonOutputParser()
FeatureBucketrocess = FeatureBucketPromptTemplate|llm|parser
# response = FeatureReviewProcess.invoke({'features':data_to_sent,'user_interests':'User is interested in travel and needs language translator'})
# print(response)
