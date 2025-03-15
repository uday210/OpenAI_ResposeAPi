import gradio as gr
from openai import OpenAI
import base64
from PIL import Image
import io

client = OpenAI()

def analyze_image(image, question):
    # Convert the image to base64 string
    if image is None:
        return "Please capture an image first."
    
    # Convert the numpy array to PIL Image
    pil_image = Image.fromarray(image)
    
    # Create a bytes buffer
    buffer = io.BytesIO()
    pil_image.save(buffer, format="PNG")
    image_bytes = buffer.getvalue()
    
    # Convert to base64
    base64_image = base64.b64encode(image_bytes).decode('utf-8')
    
    try:
        response = client.responses.create(
            model="gpt-4o",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": question
                        },
                        {
                            "type": "input_image",
                            "image_url": f"data:image/png;base64,{base64_image}"
                        }
                    ]
                }
            ]
        )
        return response.output_text
    except Exception as e:
        return f"Error analyzing image: {str(e)}"

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Image Analyzer with Webcam")
    
    with gr.Row():
        webcam = gr.Image(sources=["webcam"], label="Webcam")
        
    with gr.Row():
        question = gr.Textbox(
            label="Question",
            placeholder="What do you see in this image?",
            value="What do you see in this image?"
        )
    
    with gr.Row():
        submit_btn = gr.Button("Analyze Image")
    
    output = gr.Textbox(label="Analysis Result")
    
    submit_btn.click(
        fn=analyze_image,
        inputs=[webcam, question],
        outputs=output
    )

if __name__ == "__main__":
    demo.launch(share=True) 