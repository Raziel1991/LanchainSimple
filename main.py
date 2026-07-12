from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_agent


from tools import (
    check_internet_connection,
    check_internet_download_speed,
)

model_local_docker = ChatOpenAI(
    model_name="docker.io/ai/qwen3.6:latest",
    base_url="http://localhost:12434/v1",
    api_key="not-required",
    temperature=0
)

agent = create_agent(
    model=model_local_docker,
    tools=[
        check_internet_connection,
        check_internet_download_speed
    ],
    system_prompt="you are a helpful assistant that can check internet connection and download speed. Keep answers simple and concise. Do not make up information. If you don't know the answer, say 'I don't know' or if you cant perform the action just say 'I cannot perform that action.'"
)


# model with tools is commented out because it seems you are not using it in the current code. If you want to use the tools, you can uncomment the following lines:
# model_with_tools = model_local_docker.bind_tools(
#     [
#         check_internet_connection,
#         check_internet_download_speed
#     ]
# )



# prompt = ChatPromptTemplate.from_messages( 

#     [
#         ("system", "you are a helpful assistant that can check internet connection and download speed. Keep answers simple and concise. Do not make up information. If you don't know the answer, say 'I don't know' or if you cant perform the action just say 'I cannot perform that action.'"),
#         ("user", "{question}"),
#     ]
# )

my_question = "check my internet connection and download speed in gigabytes per second and give me a simple answer with the results."

result = agent.invoke(
        {"messages": [{"role": "user", "content": my_question}]}

)


response = result["messages"][-1]

print(response.content)


print("Input tokens:", response.usage_metadata["input_tokens"])
print("Output tokens:", response.usage_metadata["output_tokens"])
print("Total tokens:", response.usage_metadata["total_tokens"])
print("Content:", response.usage_metadata)
print("Tools used:", response.tool_calls )


