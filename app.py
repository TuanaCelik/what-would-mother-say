
from json import JSONDecodeError
import logging

import streamlit as st

from utils.haystack import run_agent, start_haystack
from utils.ui import reset_results, set_initial_state, sidebar
from utils.config import TWITTER_BEARER_TOKEN, OPENAI_API_KEY, SERPER_KEY

set_initial_state()

sidebar()

st.write("# 👩 What would they have tweeted about this?")
st.write("## About this App")
st.write("This app uses an [Agent](https://docs.haystack.deepset.ai/docs/agent) (using GPT-4) with a `WebSearch` and `TwitterRetriever` tool")
st.write("The `TwitterRetriever` is set to retrieve the latest 15 tweets by the given twitter username to construct an understanding of their style of tweeting")
st.write("### Instructions")
st.write("For best results, please provide a Twitter username as it appears on twietter. E.g.: dog_feelings 🐶")

# if st.session_state.get("OPENAI_API_KEY") and st.session_state.get("SERPER_KEY"):

agent = start_haystack(openai_key=OPENAI_API_KEY, twitter_bearer=TWITTER_BEARER_TOKEN, serper_key=SERPER_KEY)
# st.session_state["api_keys_configured"] = True

# Search bar
question = st.text_input("Example: If the twitter account tuanacelik were to write a tweet in their style about climate change, what would it be?", on_change=reset_results) 
run_pressed = st.button("Generate tweet")
# else:
#     st.write("Please provide your OpenAI and SerperDev Keys to start using the application")
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