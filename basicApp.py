from openai import OpenAI

client = OpenAI()


response = client.responses.create(
    model="gpt-4o",
    input="Write a one-sentence story about future of general AI."
)

print(response.output_text)