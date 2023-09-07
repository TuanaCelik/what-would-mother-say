import streamlit as st
from mastodon_fetcher_haystack import MastodonFetcher
from haystack.agents import Agent, Tool
from haystack.nodes import PromptNode, PromptTemplate, WebRetriever
from haystack.pipelines import WebQAPipeline


def start_haystack(openai_key, serper_key):
    prompt_node = PromptNode(
        "gpt-4",
        default_prompt_template=PromptTemplate(prompt="./prompts/lfqa.yaml"),
        api_key=openai_key,
        max_length=256,
    )

    web_retriever = WebRetriever(api_key=serper_key, top_search_results=2, mode="preprocessed_documents")
    web_pipeline = WebQAPipeline(retriever=web_retriever, prompt_node=prompt_node)

    mastodon_retriver = MastodonFetcher(last_k_posts=20)

    pn = PromptNode(model_name_or_path="gpt-4", api_key=openai_key, stop_words=["Observation:"], max_length=400)
    agent = Agent(prompt_node=pn, prompt_template="./prompts/mastodon_agent.yaml")
    
    mastodon_retriver_tool = Tool(name="MastodonRetriever", pipeline_or_node=mastodon_retriver, 
                               description="Useful for when you need to retrieve the latest posts from a username to get an understanding of their style", 
                               output_variable="documents")
    web_tool = Tool(name="WebSearch", pipeline_or_node=web_pipeline, description="Useful for when you need to research the latest about a new topic")

    agent.add_tool(mastodon_retriver_tool)
    agent.add_tool(web_tool)
    

    st.session_state["haystack_started"] = True     
    return agent                                                
    

@st.cache_data(show_spinner=True)
def run_agent(_agent, question):
    result = _agent.run(question)
    return result
