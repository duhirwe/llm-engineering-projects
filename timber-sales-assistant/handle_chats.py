import os
import json
from dotenv import load_dotenv
from openai import OpenAI

from db_functions import get_available_timber_types, get_timber_price, calculate_timber_cost
from llm_tools import get_all_tools



# Initialization

load_dotenv(dotenv_path="../.env", override=True)

openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

MODEL = "gpt-4.1-mini"
client = OpenAI()




system_message = """
You are a helpful assistant for a timber company in Rwanda.
Prices are in RWF per timber unit.
Use tools to answer questions about available timber types, unit prices, and total costs.
If the customer asks for a timber type that is not available, say so.
Give short and clear answers.
"""



def handle_tool_call(message):
    responses = []

    tool_map = {
        "get_available_timber_types": lambda args: get_available_timber_types(),
        "get_timber_price": lambda args: get_timber_price(args.get("timber_type")),
        "calculate_timber_cost": lambda args: calculate_timber_cost(
            args.get("timber_type"),
            args.get("quantity")
        ),
    }

    for tool_call in message.tool_calls:
        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        if function_name in tool_map:
            result = tool_map[function_name](arguments)
        else:
            result = f"Unknown tool: {function_name}"

        responses.append({
            "role": "tool",
            "content": result,
            "tool_call_id": tool_call.id
        })

    return responses



def chat(message, history):
    tools = get_all_tools()

    history = [{"role": h["role"], "content": h["content"]} for h in history]
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    response = client.chat.completions.create(
        model = MODEL, messages=messages, tools=tools
    )

    while response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        responses = handle_tool_call(message)
        messages.append(message)
        messages.extend(responses)
        response = client.chat.completions.create(
            model=MODEL, messages=messages, tools=tools
        )
    
    return response.choices[0].message.content