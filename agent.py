import copy
import autogen
from autogen.coding import LocalCommandLineCodeExecutor, CodeBlock
from config import LLM_CONFIG

# Setting up Assistant and User Proxy Agents
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=copy.deepcopy(LLM_CONFIG)
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "executor": LocalCommandLineCodeExecutor(work_dir="coding"),
    },
)

# message="Write a Python function that takes a list of numbers and returns the average of the numbers.",

# message="write a python for average of a list of numbers",

# Initiating Chat
chat_res = user_proxy.initiate_chat(
    assistant,
    message="write a python function for sum of two numbers",
    summary_method="reflection_with_llm",
)

print(chat_res)
