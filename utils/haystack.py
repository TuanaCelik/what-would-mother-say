import streamlit as st
import requests
from custom_nodes.tweet_retriever import TwitterRetriever
from haystack.agents import Agent, Tool
from haystack.nodes import PromptNode, PromptTemplate, WebRetriever
from haystack.pipelines import WebQAPipeline


def start_haystack(openai_key, twitter_bearer, serper_key, last_k_tweets):
    prompt_node = PromptNode(
        "text-davinci-003",
        default_prompt_template=PromptTemplate(prompt="./prompts/lfqa.yaml"),
        api_key=openai_key,
        max_length=256,
    )

    web_retriever = WebRetriever(api_key=serper_key, top_search_results=2, mode="preprocessed_documents")
    web_pipeline = WebQAPipeline(retriever=web_retriever, prompt_node=prompt_node)

    twitter_retriver = TwitterRetriever(bearer_token=twitter_bearer, last_k_tweets=last_k_tweets)

    pn = PromptNode(model_name_or_path="gpt-4", api_key=openai_key, stop_words=["Observation:"])
    agent = Agent(prompt_node=pn, prompt_template="./prompts/twitter_agent.yaml")

    tweet_retriver_tool = Tool(name="TwitterRetriever", pipeline_or_node=twitter_retriver, 
                               description="Useful for when you need to retrieve the latest tweets from a username to get an understanding of their style", 
                               output_variable="results")
    web_tool = Tool(name="WebSearch", pipeline_or_node=web_pipeline, description="Useful for when you need to research the latest about a new topic")

    agent.add_tool(tweet_retriver_tool)
    agent.add_tool(web_tool)
    

    st.session_state["haystack_started"] = True     
    return agent                                                
    

@st.cache_data(show_spinner=True)
def query(_agent, question):
    try:
        result = _agent.run(question)
    except Exception as e:
        print(e)
        result = ["Life isn't ideal sometimes and this Agent fails at doing a good job.. Maybe try another query..."]
    return result
