from toolhouse import Toolhouse
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

# Set API key
os.environ["TOOL_HOUSE_KEY"] = os.getenv("TOOL_HOUSE_KEY")

th = Toolhouse(
    provider="anthropic", access_token=os.environ["TOOL_HOUSE_KEY"]
)
client = Anthropic()

print(os.environ["TOOL_HOUSE_KEY"])

def llm_call(messages: list[dict]):
    return client.messages.create(
        model="claude-3-5-sonnet-20240620",
        system="Respond directly, do not preface or end your responses with anything.",
        max_tokens=1000,
        messages=messages,
        tools=th.get_tools(),
    )


messages = [
    {
        "role": "user",
        "content": "Get the contents of https://toolhouse.ai and summarize its key value propositions in three bullet points.",
    },
]

response = llm_call(messages)
messages += th.run_tools(response, append=True)
final_response = llm_call(messages)
print(final_response.content[0].text)
