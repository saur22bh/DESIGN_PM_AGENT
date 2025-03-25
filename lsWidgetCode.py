from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from langchain_anthropic import ChatAnthropic
import os 
import streamlit as st
os.environ["ANTHROPIC_API_KEY"] = st.secrets["ANTHROPIC_API_KEY"]

llm = ChatAnthropic(model='claude-3-5-sonnet-20241022',
default_headers={
        "anthropic-beta": "max-tokens-3-5-sonnet-2024-07-15"
    },
    max_tokens=8192
                    )

prompt = '''
 Design a set of three visually striking and highly engaging mobile lock screen widgets in React using Tailwind CSS or HTML, serving as the primary entry point to a mobile based native website for which description is provided.
The widgets should align with the website: {description}. They should come in three sizes—small 108x96 px, medium 212x96 px, and large 328x96 px. Do include images if reqd. Each widget should be aesthetically compelling.
The goal is to create widgets so visually engaging that users feel compelled to click and explore the website further.
Output Format:   
   -  Only return the code  as output and nothing else.  No explanations, comments, or instructions  should be included.   
'''
desc = '''
Mindful Moments: Integrated Meditation Experience
A seamlessly integrated meditation tool that combines guided timer functionality with breathing visualization and progress tracking in a single, vertically scrollable interface.

Flow Overview
As you open the page, you're presented with a calming interface that flows naturally from top to bottom:

Section 1: Session Setup
A large, serene meditation timer displayed prominently
Time selection with elegant slider (1-120 minutes)
Quick presets (5, 10, 15, 30 min) as tappable bubbles
Ambient sound selection below (forest, rain, singing bowls, silence) with subtle preview on tap
Optional interval bell settings that expand when activated
Vibration toggle for eyes-closed practice
Section 2: Breathing Guide
As you scroll down, the breathing visualization fades into view
Animated circle that expands and contracts to guide your breath
Simple pattern selector (4-7-8 breathing, box breathing, diaphragmatic)
Visualization style options (circle, wave, or line pattern)
Speed adjustment slider with subtle haptic feedback option
"Follow Breath" button that expands the visualization to full screen mode
Section 3: Practice Insights
Calendar view showing your meditation streak with highlighted current day
Week-at-a-glance visualization showing session duration as varying height bars
Upcoming milestone notification ("3 more days until your 10-day streak!")
Recent session stats (average duration, most used technique)
Voice journaling button that expands to reveal quick emotion tagging and voice-to-text reflection option
Experience Details
A gentle "Begin Practice" button floats at the bottom of the initial view
When meditation starts, the screen transitions to your chosen breathing visualization with timer overlay
Post-session, the screen automatically scrolls to the insights section with an animation celebrating your completed session
Pull-to-refresh at the top reveals a "mindful moment" - a quick breathing exercise or mindfulness prompt
Subtle haptic feedback and ambient sounds respond to your scrolling, creating a tactile, immersive experience
Accessibility features include voice guidance options and high-contrast visualization modes
The continuous scrolling design maintains a sense of flow that mirrors the meditation experience itself, moving naturally between preparation, practice, and reflection.
'''
lsWidgetCodePromptTemplate = PromptTemplate(template=prompt,input_variables=['description'])
parser = StrOutputParser()
lsWidgetCodeProcess = lsWidgetCodePromptTemplate|llm|parser

