---
title: What would mother say?
emoji: 🫶
colorFrom: pink
colorTo: yellow
sdk: streamlit
sdk_version: 1.21.0
app_file: app.py
pinned: false
---

# What would mother say?

This app includes a Haystack agent with access to 2 tools:
- `TweetRetriever`: Useful for when you need to retrive the latest tweets from a username to get an understanding of their style
- `WebSearch`: Useful for when you need to research the latest about a new topic

We build an Agent that aims to first understand the style in which a username tweets. Then, it uses the WebSearch tool to gain knowledge on a topic that the LLM may not have info on, to generate a tweet in the users style about that topic.
### Try it out on [🤗 Spaces](https://huggingface.co/spaces/Tuana/what-would-mother-say)

##### A showcase of a Haystack Agent with a custom `TwitterRetriever` Node and a `WebQAPipeline` as tools.

**Custom Haystack Node**

This repo contains a streamlit application that given a query about what a certain twitter username would post on a given topic, generates a tweet in their style (or tries to). It does so by using a custom Haystack node I've built called the [`TweetRetriever`](/custom_nodes/tweet_retriever.py)

**Custom PromptTemplates**

It's been built with [Haystack](https://haystack.deepset.ai) using the [`Agent`](https://docs.haystack.deepset.ai/docs/agent) and by creating a custom [`PromptTemplate`](https://docs.haystack.deepset.ai/docs/prompt_node#templates)

All the prompt templates used in this demo, both for the `WebQAPipeline` and the `Agent` can be found in `./prompts`.

<img width="867" alt="image" src="https://github.com/TuanaCelik/what-would-mother-say/assets/15802862/b05f8bde-8fd5-4c6f-beac-1578437a145b">

## To learn more about the Agent

Check out our tutorial on the Conversational Agent [here](https://haystack.deepset.ai/tutorials/24_building_chat_app)

## Installation and Running
1. Install requirements:
`pip install -r requirements.txt`
2. Run the streamlit app:
`streamlit run app.py`
3. Createa a `.env` and add your Twitter Bearer token, OpenAI Key, and SerperDev Key:
`TWITTER_BEARER_TOKEN`
`SERPER_KEY`
`OPENAI_API_KEY`

This will start up the app on `localhost:8501` where you will find a simple search bar

#### The Haystack Community is on [Discord](https://discord.com/invite/VBpFzsgRVF)
