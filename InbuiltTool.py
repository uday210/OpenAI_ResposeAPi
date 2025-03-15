from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    tools=[{"type": "web_search_preview"}],
    input="give me details about trailhead Dx 2025",
    stream=False
)

print(response.output_text) # use when stream=False

# Stream response when Stream=True
'''
for chunk in response:
    print(chunk.output_text)
'''
