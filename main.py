from dotenv import load_dotenv
from autogen import config_list_from_json
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent
from autogen import UserProxyAgent
import os


# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# config_list = config_list_from_json("OAI_CONFIG_LIST")

config_list = [
    {
        'model': 'gpt-3.5',
        'api_key': OPENAI_API_KEY,
    },
]

#Creating the GPT assistant agent
gpt_assistant = GPTAssistantAgent(
    name="assistant",
    llm_config={
        "config_list": config_list,
        "assistant_id": None
    })

#Setting Up the UserProxyAgent
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config={
        "work_dir": "coding"
    },
    human_input_mode="NEVER")

#Initiating the Task
user_proxy.initiate_chat(gpt_assistant, message="code to connect an assistant to documents stored in openai account storage")

#Enabling Advanced Features
gpt_assistant = GPTAssistantAgent(
    name="assistant",
    llm_config={
        "config_list": config_list,
        "assistant_id": None,
        "tools": [{"type": "code_interpreter"}],
    })

#Test Agent
user_proxy.initiate_chat(gpt_assistant, message="Get the price of gold and print a visual of the last 4 days closing price")