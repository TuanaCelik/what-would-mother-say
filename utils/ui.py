import streamlit as st
from PIL import Image

def set_state_if_absent(key, value):
    if key not in st.session_state:
        st.session_state[key] = value

def set_initial_state():
    set_state_if_absent("question", "Provide a Twitter username")
    set_state_if_absent("result", None)
    set_state_if_absent("haystack_started", False)

def reset_results(*args):
    st.session_state.result = None

# def set_openai_api_key(api_key: str):
#     st.session_state["OPENAI_API_KEY"] = api_key

# def set_serper_dev_key(api_key: str):
#     st.session_state["SERPER_KEY"] = api_key

def sidebar():
    with st.sidebar:
        image = Image.open('logo/haystack-logo-colored.png')
        st.markdown("Thanks for coming to this 🤗 Space.\n\n"
        "This is a project for fun and is a sister to the [should-i-follow](https://huggingface.co/spaces/deepset/should-i-follow) Space."
        " There's a lot that can be improved to make this app better.\n\n"
        "**Take results with a grain of** 🧂\n\n"
        "")

        st.markdown(
            "## How to use\n"
            # "1. Enter your [OpenAI API](https://platform.openai.com/account/api-keys) and [SerperDev API](https://serper.dev/) keys below\n"
            "1. Enter a query that includes a Mastodon username and be descriptive about wanting a post as a result.\n"
            "2. Enjoy 🤗\n"
        )

        # openai_api_key_input = st.text_input(
        #     "OpenAI API Key",
        #     type="password",
        #     placeholder="Paste your OpenAI API key here (sk-...)",
        #     help="You can get your API key from https://platform.openai.com/account/api-keys.",
        #     value=st.session_state.get("OPENAI_API_KEY", ""),
        # )

        # serper_api_key_input = st.text_input(
        #     "SerperDev API Key",
        #     type="password",
        #     placeholder="Paste your SerperDev API key here (sk-...)",
        #     help="You can get your API key from https://serper.dev.",
        #     value=st.session_state.get("SERPER_KEY", ""),
        # )

        # if openai_api_key_input:
        #     set_openai_api_key(openai_api_key_input)
        
        # if serper_api_key_input:
        #     set_serper_dev_key(serper_api_key_input)

        st.markdown("---")
        st.markdown(
            "## How this works\n"
            "This app was built with [Haystack](https://haystack.deepset.ai) using the"
            " [`Agent`](https://docs.haystack.deepset.ai/docs/agent) custom [`PromptTemplates`](https://docs.haystack.deepset.ai/docs/prompt_node#templates)\n\n"
            "as well as a custom `MastodonFetcher` node\n"
            " The source code is also on [GitHub](https://github.com/TuanaCelik/what-would-mother-say)"
            " with instructions to run locally.\n"
            "You can see how the `Agent` was set up [here](https://github.com/TuanaCelik/what-would-mother-say/blob/main/utils/haystack.py)")
        st.markdown("---")
        st.markdown("Made by [tuanacelik](https://twitter.com/tuanacelik)")
        st.markdown("---")
        st.markdown("""Thanks to [mmz_001](https://twitter.com/mm_sasmitha) 
                        for open sourcing [KnowledgeGPT](https://knowledgegpt.streamlit.app/) which helped me with this sidebar 🙏🏽""")
        st.image(image, width=250)