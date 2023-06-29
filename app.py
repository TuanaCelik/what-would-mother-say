
from annotated_text import annotation
from json import JSONDecodeError
import logging
from markdown import markdown
import requests

import streamlit as st
from utils.haystack import run_agent
from utils.ui import reset_results, set_initial_state, sidebar
from utils.config import TWITTER_BEARER_TOKEN, SERPER_KEY, OPENAI_API_KEY

set_initial_state()

sidebar()

st.write("# 👩 What would they have tweeted about this?")

# if st.session_state.get("OPENAI_API_KEY"):
if "last_k_tweets" not in st.session_state:
    st.session_state["last_k_tweets"] = st.slider("How many tweets should we retrieve?", value=10, step=10, max_value=100, min_value=10, on_change = reset_results)

agent = start_haystack(openai_key=OPENAI_API_KEY, twitter_bearer=TWITTER_BEARER_TOKEN, serper_key=SERPER_KEY, last_k_tweets=st.session_state["last_k_tweets"])
# st.session_state["api_keys_configured"] = True

# Search bar
question = st.text_input("Example: If the twitter account tuanacelik were to write a tweet in their style about climate change, what would it be?", on_change=reset_results) 
run_pressed = st.button("Generate tweet")
# else:
#     st.write("Please provide your OpenAI Key to start using the application")
#     st.write("If you are using a smaller screen, open the sidebar from the top left to provide your OpenAI Key 🙌")

# if st.session_state.get("api_keys_configured"):
run_query = (
    run_pressed or question != st.session_state.question
)
if run_query and question:
    reset_results()
    st.session_state.question = question
    try:
        st.session_state.result = run_agent(agent, question)
    except JSONDecodeError as je:
        st.error(
            "👓 &nbsp;&nbsp; An error occurred reading the results. Is the document store working?"
        )    
    except Exception as e:
        logging.exception(e)
        st.error("🐞 &nbsp;&nbsp; An error occurred during the request.")            
            
if st.session_state.result:
    result = st.session_state.result
    st.write(result["answers"][0].answer)
            
