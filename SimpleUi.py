from openai import OpenAI
import gradio as gr


client = OpenAI()

def ask_ai(question):
    response = client.responses.create(
        model="gpt-4o",
        input=question)
    
    return response.output_text

app = gr.Interface(fn=ask_ai, inputs="text", outputs="text", title="Ask AI", description="Ask AI any question and get an answer.")
app.launch()

