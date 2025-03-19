from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()
from langchain_anthropic import ChatAnthropic
# llm = ChatOllama(model='llama3.2')
llm = ChatAnthropic(model='claude-3-7-sonnet-20250219')

prompt = '''
Evaluate the reviewed product features and score each based on:

1️⃣ Mobile Usability (1-10) → How well does this feature work on a mobile webpage? Consider responsiveness, ease of use, and mobile-first design principles.

2️⃣ User Engagement (1-10) → Will this feature enhance user interaction and retention? Give a higher score if the feature strongly aligns with the user’s interests and encourages frequent interaction or long-term engagement.

3️⃣ Practicality (1-10) → How feasible is it to implement this feature effectively? Consider technical complexity, required resources, and real-world applicability.

For each feature, provide:

A total score (sum of all three criteria).
A rank based on the total score (higher scores are ranked higher).
No two features can have same rank, if two features are having same total score, do a tie breaker basis higher engagement score.

Input:
User Interests: {user_interests}
Reviewed Product Features: {generated_features}
Note : Make sure the description returned for every feature is same as what was given in input for that feature.
Output Format:
📌 Dictionary Format as mentioned below in example:
{{
    "Feature A": {{"rank": 1, "mobile_usability": mobile_usability_score, "engagement": engagement_score, "practicality": practicality_score, "total_score": total_score,"description" : featureDescription}},
    "Feature B": {{"rank": 2, "mobile_usability": mobile_usability_score, "engagement": engagement_score, "practicality": practicality_score, "total_score": total_score,"description" : featureDescription}}
}}
'''

daat = {
  "Highly Relevant": [
    {
      "feature_name": "Smart Translator",
      "description": "Real-time camera translation of signs, menus, and documents Offline language packs for common travel destinations Voice-to-voice translation for conversations with locals Phrasebook with common travel expressions organized by situation (restaurant, hotel, emergency)",
      "reason": "Directly aligns with user's need for a language translator"
    },
    {
      "feature_name": "Destination Language Prep",
      "description": "Pre-trip language crash courses based on upcoming travel destinations Daily 5-minute language lessons tailored to planned activities Interactive pronunciation guide with feedback Cultural etiquette tips alongside language learning",
      "reason": "Meets user's need for language preparation and cultural context"
    },
    {
      "feature_name": "Travel Itinerary Language Assistant",
      "description": "Scan and auto-translate booking confirmations and travel documents Suggest key phrases needed for each day's activities Emergency phrase generator with audio for urgent situations Location-based translation suggestions that change as you travel",
      "reason": "Directly supports user's need for language assistance while traveling"
    },
    {
      "feature_name": "Digital Travel Journal",
      "description": "Document your travel with auto-translated local phrases and words Tag photos with local language descriptions Track language progress across different destinations Share multilingual travel stories with friends and community",
      "reason": "Aligns with user's need to document their travels and track language progress"
    }
  ],
  "Somewhat Relevant": [
    {
      "feature_name": "Destination Language Prep",
      "description": "Pre-trip language crash courses based on upcoming travel destinations Daily 5-minute language lessons tailored to planned activities Interactive pronunciation guide with feedback Cultural etiquette tips alongside language learning",
      "reason": "While relevant, the user may not need daily language lessons, but the pre-trip crash course and phrasebook are useful"     
    },
    {
      "feature_name": "Local Experience Finder",
      "description": "Discover authentic local experiences with language difficulty ratings Connect with language exchange partners at your destination Filter activities by language accessibility (English spoken, translation available, etc.) Community reviews from travelers with similar language backgrounds",
      "reason": "Not directly aligned with user's primary need for a language translator"
    },
    {
      "feature_name": "Cultural Context Companion",
      "description": "Learn cultural context alongside language (gestures, customs, taboos) AR overlay explaining cultural significance of landmarks and objects Local slang and idiom guide for each destination Region-specific etiquette tips to avoid cultural misunderstandings",  
      "reason": "While relevant, the user may not need in-depth cultural knowledge at all times"
    },
    {
      "feature_name": "Global Payment Helper",
      "description": "Currency converter with visual price comparisons to home country Translated explanations of local payment systems and tipping customs Expense tracking with local and home currency Payment-related phrase guide for shopping and restaurants",
      "reason": "Not directly aligned with user's primary need for a language translator"
    }
  ],
  "Not Relevant": [
    {
      "feature_name": "Local Experience Finder",
      "description": "Discover authentic local experiences with language difficulty ratings Connect with language exchange partners at your destination Filter activities by language accessibility (English spoken, translation available, etc.) Community reviews from travelers with similar language backgrounds",
      "reason": "Does not directly align with user's need for a language translator"
    },
    {
      "feature_name": "Cultural Context Companion",
      "description": "Learn cultural context alongside language (gestures, customs, taboos) AR overlay explaining cultural significance of landmarks and objects Local slang and idiom guide for each destination Region-specific etiquette tips to avoid cultural misunderstandings",  
      "reason": "Does not directly align with user's primary need for a language translator"
    },
    {
      "feature_name": "Global Payment Helper",
      "description": "Currency converter with visual price comparisons to home country Translated explanations of local payment systems and tipping customs Expense tracking with local and home currency Payment-related phrase guide for shopping and restaurants",
      "reason": "Does not directly align with user's primary need for a language translator"
    }
  ]
}

daat = 'Features : ' + "\n".join([f"- {f['feature_name']}: {f['description']}" for f in daat['Highly Relevant']])


   


FeatureRankPromptTemplate = PromptTemplate(template=prompt,input_variables=['user_interests','generated_features'])
parser = JsonOutputParser()
FeatureRankingProcess = FeatureRankPromptTemplate|llm|parser
# response = FeatureRankingProcess.invoke({'user_interests':'User is interested in travel and needs language translator','generated_features':daat})
# print(response)




