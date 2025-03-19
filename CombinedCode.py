from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()
from langchain_anthropic import ChatAnthropic
llm = ChatOllama(model='llama3.2')

llm = ChatAnthropic(model='claude-3-7-sonnet-20250219',
default_headers={
        "anthropic-beta": "max-tokens-3-5-sonnet-2024-07-15"
    },
    max_tokens=8192
                    )

prompt = '''
Given the following description of a mobile-native webpage, create a one-page mobile web UI.   
 Inputs:   
Feature Description: {Featuredescription}  

###  Key Requirements:   

1.  Tech Stack Selection:   
   - Decide whether to generate the code in  React (with Tailwind/inline CSS) or plain HTML/CSS/JS , based on the description and complexity of interactions.  
   - Ensure the choice is  optimal for a mobile-native webpage .  

2.  Design & Styling:   
   -  Dark Theme Requirement  → The UI should have a dark background [choose best dark background colour basis feature description] . Choose color themes for text and background accordingly to ensure  high readability and good contrast .  
   -  Fully self-contained files  → The code for each page should be in  one file only , meaning styling (CSS/Tailwind) and scripting (JS/React logic) should be included within the same file. No external CSS or JS files.  
   -  Component Reusability Allowed  → If React is chosen, you can use external libraries and components (e.g., `@/components/ui/card`, `shadcn/ui`, or other UI libraries) to streamline the design. Import necessary components as needed, but ensure the final code is functional and well-structured.  

3.  Error-Free Code:   
   - Ensure the generated code is  functional  and free of  syntax or runtime errors .  

4.  Visually Appealing Design:   
   - Choose  color themes  that align with a  dark UI  while ensuring  good contrast, readability, and aesthetics .  

5.  Attractiveness Check Before Output:   
   - Before returning the code,  ensure the UI is attractive and well-optimized for a dark theme .  

6.  Output Format:   
   -  Only return the code  as output and nothing else.  No explanations, comments, or instructions  should be included.

   
'''

parser = StrOutputParser()

CombinedCodePromptTemplate = PromptTemplate(template=prompt,input_variables=['Featuredescription'])


CombinedCodeProcess = CombinedCodePromptTemplate|llm|parser 
description = '''
Here's a description of the new feature, tailored to a one-page mobile webpage with a scrollable interaction model:

**Feature Name:** Fitness Journey Companion

**Tagline:** Track your progress, stay motivated, and connect with like-minded individuals.

**Description:**
Find inspiration and motivation on your fitness journey with our companion app. Get personalized quotes, track your workouts, and reflect on your progress in one easy-to-use interface.

**How it Works:**

1. **Workout Journal**: Log your workouts, note improvements, and set reminders for upcoming sessions.
2. **Daily Motivation**: Receive daily motivational quotes tailored to your fitness goals or current workout.
3. **Progress Tracking**: View your progress over time, including workouts completed, miles ran, or weight lifted.

**Content:**

* A scrollable timeline showcasing your workouts, with the option to add notes and photos.
* A section for daily motivational quotes, with a photo and a brief quote.
* A section for tracking progress, showing your improvements and milestones achieved.
* A call-to-action (CTA) button to connect with like-minded individuals through our Workout Buddy feature.

**Design:**

* Use a clean and modern design with a color scheme that evokes feelings of motivation and wellness (e.g., blues and greens).
* Incorporate illustrations or graphics that represent fitness and motivation, such as running shoes, dumbbells, or inspirational quotes.
* Use a scrollable interface to showcase the content in a continuous vertical flow, making it easy for users to navigate through their progress.

**Interactions:**

* When a user scrolls down the page, new content is revealed, creating a sense of discovery and exploration.
* Clicking on a motivational quote opens a modal window with more information about the quote, such as its origin or meaning.
* Connecting with Workout Buddies is done via a seamless integration, allowing users to share their progress and receive support from others.

**Technical Requirements:**

* Use a responsive design to ensure the app works perfectly on various screen sizes and devices.
* Implement animations and transitions to enhance the user experience.
).
* Incorporate illustrations or graphics that represent fitness and motivation, such as running shoes, dumbbells, or inspirational quotes.
* Use a scrollable interface to showcase the content in a continuous vertical flow, making it easy for users to navigate through their progress.

**Interactions:**

* When a user scrolls down the page, new content is revealed, creating a sense of discovery and exploration.
* Clicking on a motivational quote opens a modal window with more information about the quote, such as its origin or meaning.
* Connecting with Workout Buddies is done via a seamless integration, allowing users to share their progress and receive support from others.

**Technical Requirements:**

* Use a responsive design to ensure the app works perfectly on various screen sizes and devices.
* Implement animations and transitions to enhance the user experience.
**Interactions:**

* When a user scrolls down the page, new content is revealed, creating a sense of discovery and exploration.
* Clicking on a motivational quote opens a modal window with more information about the quote, such as its origin or meaning.
* Connecting with Workout Buddies is done via a seamless integration, allowing users to share their progress and receive support from others.

**Technical Requirements:**

* Use a responsive design to ensure the app works perfectly on various screen sizes and devices.
* Implement animations and transitions to enhance the user experience.
* Implement animations and transitions to enhance the user experience.
* Ensure the app is optimized for fast loading times and smooth scrolling.
'''
# response = CombinedCodeProcess.invoke({'Featuredescription':description})
# print(response)