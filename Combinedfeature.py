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
list_of_features = '''
Feature List:

Workout Buddy
Description: Find and connect with like-minded individuals for fitness motivation and accountability.
How it works: Users can browse a list of available workout buddies in their area or within a specific distance range. They can filter by interest, fitness level, or time commitment. Once connected, users can schedule workouts together and track progress.
Nutrition Insights
Description: Get personalized nutrition advice based on your dietary needs and goals.
How it works: Users take a short quiz to determine their nutritional requirements, allergies, and preferences. The app provides tailored meal plans, ingredient lists, and grocery shopping suggestions.
Step Challenge
Description: Set daily step goals and compete with friends for healthy competition.
How it works: Users can set a daily step goal and earn rewards as they reach milestones. The app also tracks progress against global leaders or friends' challenges.
Mood Tracker
Description: Monitor your emotions to better understand your fitness journey.
How it works: Users can log their moods, track patterns, and receive personalized insights on how exercise impacts their mental well-being.
Healthy Recipes
Description: Discover nutritious recipes based on your dietary needs and preferences.
How it works: Users browse a curated list of healthy recipes with ingredients, cooking times, and nutritional information. They can filter by cuisine, ingredient availability, or cooking time.
Fitness Journal
Description: Record your workouts, track progress, and reflect on your journey.
How it works: Users can log their workouts, note improvements, and set reminders for upcoming sessions. The app also provides a reflection section to evaluate progress and set new goals.
Motivational Quotes
Description: Find daily motivation with inspiring quotes tailored to your fitness journey.
How it works: Users receive daily motivational quotes related to their fitness goals or current workout. The quote is accompanied by a photo, and users can save their favorites for later reference.
Community Forum
Description: Engage with like-minded individuals in a supportive community forum.
How it works: Users can browse a discussion forum where they can ask questions, share success stories, or seek advice from other fitness enthusiasts.
'''
# response = CombinedFeatureProcess.invoke({'list_of_features':list_of_features,'user_interest':'Health and Fitness'})
# print(response)