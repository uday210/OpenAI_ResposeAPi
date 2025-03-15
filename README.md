# OpenAI API Examples

This repository contains various examples demonstrating the usage of OpenAI's API with Python. The examples include basic API calls, chat interfaces, AI agents implementation, and image analysis.

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Webcam (for image analysis example)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

3. Install required packages:
```bash
pip install openai gradio openai-agents pillow
```

4. Set up your OpenAI API key:
```bash
# On Windows
set OPENAI_API_KEY=your-api-key-here

# On macOS/Linux
export OPENAI_API_KEY=your-api-key-here
```

## Examples

### 1. Basic API Call (basicApp.py)
A simple example that generates a one-sentence story about the future of general AI.
```bash
python basicApp.py
```

### 2. Web Search Tool (InbuiltTool.py)
Demonstrates the usage of OpenAI's web search preview tool.
```bash
python InbuiltTool.py
```

### 3. Chat Interface (ChatBotApp.py)
A Gradio-based chat interface for interacting with the AI.
```bash
python ChatBotApp.py
```

### 4. Simple UI (SimpleUi.py)
A basic Gradio interface for question-answering.
```bash
python SimpleUi.py
```

### 5. Language Agents (OpenAiAgent.py)
Implementation of AI agents that can communicate in different languages.
```bash
python OpenAiAgent.py
```

### 6. Salesforce Team Simulation (SfdcTeam.py)
Simulates a Salesforce development team with different roles using AI agents.
```bash
python SfdcTeam.py
```

### 7. Webcam Image Analyzer (WebcamAnalyzer.py)
A Gradio interface that captures images from your webcam and analyzes them using OpenAI's vision model. This example allows you to:
- Capture images from your webcam
- Ask questions about the captured image
- Get AI-powered analysis of the image
```bash
python WebcamAnalyzer.py
```

## Note
- Make sure to replace `your-api-key-here` with your actual OpenAI API key
- The model names used in the examples should match the models available in your OpenAI account
- The web interface examples (ChatBotApp.py, SimpleUi.py, and WebcamAnalyzer.py) will launch a local server that you can access through your web browser
- For the WebcamAnalyzer example, ensure you have a working webcam and proper permissions for browser access
