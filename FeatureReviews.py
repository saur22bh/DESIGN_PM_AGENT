from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_ollama import ChatOllama

from langchain_anthropic import ChatAnthropic
llm = ChatOllama(model='llama3.2')

llm = ChatAnthropic(model='claude-3-7-sonnet-20250219')

prompt = '''
You are an expert in product development and mobile web applications. Your task is to refine a list of product features by strictly applying the following two filters:

Relevance to Interest: Remove any feature that does not align with the stated interests. If a feature does not directly serve the user’s needs, exclude it.
Suitability for Mobile Native Web Applications: Eliminate any feature that is not technically feasible, practical, or optimized for a mobile web application. This includes features that require excessive computational power, are incompatible with mobile browsers, or demand hardware access that mobile web apps cannot provide.

Note : Descriptions for each feature is also provided in features list.
Note : Make sure that same feature does not fall under both continued features and eliminated features.
Input:
Topic: {user_interests}
Generated Product Features: {generated_features}

Note : Make sure the description returned for every feature is same as what was given in input for that feature.

Respond only in the following JSON format and strictly follow key names.
{{
  "continued_features": [
    {{
      "feature_name": "Feature1",
      "description": "Detailed description of Feature1",
      "reason": "Reason for inclusion"
    }},
    {{
      "feature_name": "Feature2",
      "description": "Detailed description of Feature2",
       "reason": "Reason for inclusion"    
    }}
  ],
  eliminated_features: [
    {{
      "feature_name": "FeatureX",
      "description": "Detailed description of FeatureX",
      "reason": "Reason for elimination"
    }},
    {{
      "feature_name": "FeatureY",
      "description": "Detailed description of FeatureY",
      "reason": "Reason for Elimination"
    }}
  ]
}}
'''

FeatureReviewPromptTemplate = PromptTemplate(template = prompt,
                                             input_variables = ['user_interests','generated_features']
                                             )

parser = JsonOutputParser()

FeatureReviewProcess = FeatureReviewPromptTemplate|llm|parser 




# response = FeatureReviewProcess.invoke({'user_interests':'User is interested in travel and knows the importance of language translator while travelling','generated_features':"""Personalized Native Mobile Webpage Features
# Based on the user's interest in travel and their understanding of the importance of language translation while traveling, I'll design features that directly address these needs while also suggesting complementary features they might enjoy.
# Core Features

# Smart Translator

# Real-time camera translation of signs, menus, and documents
# Offline language packs for common travel destinations
# Voice-to-voice translation for conversations with locals
# Phrasebook with common travel expressions organized by situation (restaurant, hotel, emergency)


# Destination Language Prep

# Pre-trip language crash courses based on upcoming travel destinations
# Daily 5-minute language lessons tailored to planned activities
# Interactive pronunciation guide with feedback
# Cultural etiquette tips alongside language learning


# Travel Itinerary Language Assistant

# Scan and auto-translate booking confirmations and travel documents
# Suggest key phrases needed for each day's activities
# Emergency phrase generator with audio for urgent situations
# Location-based translation suggestions that change as you travel


# Local Experience Finder

# Discover authentic local experiences with language difficulty ratings
# Connect with language exchange partners at your destination
# Filter activities by language accessibility (English spoken, translation available, etc.)
# Community reviews from travelers with similar language backgrounds


# Cultural Context Companion

# Learn cultural context alongside language (gestures, customs, taboos)
# AR overlay explaining cultural significance of landmarks and objects
# Local slang and idiom guide for each destination
# Region-specific etiquette tips to avoid cultural misunderstandings


# Digital Travel Journal

# Document your travel with auto-translated local phrases and words
# Tag photos with local language descriptions
# Track language progress across different destinations
# Share multilingual travel stories with friends and community


# Smart Packing Assistant

# Destination-specific packing recommendations
# Language resources checklist (phrasebooks, translation tools)
# Cultural adaptation items (appropriate clothing for religious sites, etc.)
# Local tech compatibility guide (power adapters, SIM card information)


# Global Payment Helper

# Currency converter with visual price comparisons to home country
# Translated explanations of local payment systems and tipping customs
# Expense tracking with local and home currency
# Payment-related phrase guide for shopping and restaurants

# """

# })




# formatted_features = "\n".join([f"- {f['feature_name']}: {f['description']}" for f in response['continued_features']])

# data_to_sent = 'Features along with their descriptions : '+ '\n' + formatted_features                                        
# print(data_to_sent)