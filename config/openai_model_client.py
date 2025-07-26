# https://microsoft.github.io/autogen/stable//user-guide/agentchat-user-guide/tutorial/models.html#azure-openai

from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
from config.constants import MODEL_OPENAI
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')


def get_model_client():
    openai_model_client = OpenAIChatCompletionClient(
        model=MODEL_OPENAI,
        api_key= api_key
    )

    return openai_model_client