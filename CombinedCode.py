from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()
from langchain_anthropic import ChatAnthropic


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
