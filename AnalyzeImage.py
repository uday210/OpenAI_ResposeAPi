from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    input=[
        {"role": "user", "content": "what you see in this image?"},
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    "image_url": "https://www.salesforce.com/news/wp-content/uploads/sites/3/2024/09/Salesforce-Winter-25-Release_-Agentforce-Agents-New-Connectors-for-Data-Cloud-and-More-1.png?w=1024&h=576"
                }
            ]
        }
    ]
)

print(response.output_text)