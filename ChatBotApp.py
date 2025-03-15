import gradio as gr
from openai import OpenAI

client = OpenAI()

def askAi(question,history):
    response = client.responses.create(
        model="gpt-4o",
        input=question
    )

    return response.output_text

app = gr.ChatInterface(fn=askAi, type="messages", title="Ask AI", description="Ask AI any question and get an answer.")
app.launch()