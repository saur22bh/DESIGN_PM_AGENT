
# import streamlit as st
# from graphs import graph_compiled
# from codeModifier import CodeModifierProcess 


# st.title('Product Features, SHP UI code and LockScreen : XS,M and L widget UI code')

# UserInterest = st.text_input("Enter an user interest, topic or them basis which you would like me to generate product features and UI code")
# if st.button("Generate Features and Description"):
#     if UserInterest:
#         st.write('Thanks for user interest, hold on for some exciting features and UI')
#         output = graph_compiled.invoke({'UserInterest':UserInterest}) # Execute LangGraph function
#         st.write('### Description for Combined Feature')
#         st.write(output['CombinedFeatureDescription'])
#         st.write('### Code for above feature')
#         st.write(output['Code'])
#         Modifications = st.text_input('Any modifications Needed?')
#         if st.button('Modify'):
#             if Modifications:
#                st.write('### Modifying current code, new code loading')
#                NewScript =  CodeModifierProcess.invoke({'Original':output['Code'],'instrubctions':Modifications})
#                st.write('''### Here's the updated code''')
#                st.write(NewScript)
#             else:
#                 st.warning('Pls enter any modifications that you desire to be implemented')   

#     else:
#         st.warning("Please enter some text.")







import streamlit as st
from graphs import graph_compiled
from codeModifier import CodeModifierProcess 
from lsWidgetCode import lsWidgetCodeProcess
import pandas as pd
import streamlit as st

st.title('Feature Ideation, UI code for SHP and LS Widgets')

# Store output in session state to persist it across reruns
if 'output' not in st.session_state:
    st.session_state.output = None
if 'new_script' not in st.session_state:
    st.session_state.new_script = None
if 'ls' not in st.session_state:
    st.session_state.ls = None  
if 'CombinedFeatureDescription' not in st.session_state:
    st.session_state.CombinedFeatureDescription = None
if 'Code' not in st.session_state:
    st.session_state.Code = None

UserInterest = st.text_input("Enter a user interest/topic based on which you would like me to generate product features and UI code")

st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #001F3F; /* Navy Blue */
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    div.stButton > button:first-child:hover {
        background-color: #003366; /* Darker Navy Blue */
    }
    </style>
""", unsafe_allow_html=True)

if st.button("Generate Features and UI Code"):
    if UserInterest:
        st.write('Thanks for the input')
        st.write('Ideating features and generating code')
        st.session_state.output = graph_compiled.invoke({'UserInterest': UserInterest})  # Execute LangGraph function

if st.session_state.output:
    output = st.session_state.output  # Store in a variable to prevent multiple calls

    st.write('### Features generated')
    st.write(output['FeaturesGenerated'])

    df = pd.DataFrame.from_dict(output['FeaturesRanked'], orient='index')
    df = df.drop(columns=['description'])
    st.title("Features Ranked")
    st.dataframe(df) 

    if st.button('Tap to see code and feature description for a feature created by combining 2-3 features'):
        st.session_state.CombinedFeatureDescription = output['CombinedFeatureDescription']
        st.session_state.Code = output['Code']

if st.session_state.CombinedFeatureDescription and st.session_state.Code:
    st.write('### Description for combined feature [feature made combining some of the above features]')
    st.write(st.session_state.CombinedFeatureDescription)
    st.write('### Code for above feature')
    st.write(st.session_state.Code)  # Display as HTML

    # Input for modifications
    Modifications = st.text_input('Any modifications needed?')

    if st.button('Modify'):
        if Modifications:
            st.write('### Modifying current code')
            st.session_state.new_script = CodeModifierProcess.invoke({'Original': st.session_state.Code, 'instrubctions': Modifications})

    if st.button('See LS Widget UI Code'):
        st.write('### Loading ...')
        st.session_state.ls = lsWidgetCodeProcess.invoke({'description': st.session_state.CombinedFeatureDescription})

if st.session_state.new_script:
    st.write('### Here’s the updated code')
    st.write(st.session_state.new_script)  # Display as HTML

if st.session_state.ls:
    st.write('### LS Widget Code')
    st.write(st.session_state.ls)    
