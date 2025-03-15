I'll help you add the complete README.md file to your project. Since the file appears unchanged, I'll provide the complete contents again:

```markdown:README.md
# OpenAI API Examples

This repository contains various examples demonstrating the usage of OpenAI's API with Python. The examples include basic API calls, chat interfaces, and AI agents implementation.

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

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
pip install openai gradio openai-agents
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

## Note
- Make sure to replace `your-api-key-here` with your actual OpenAI API key
- The model "gpt-4o" used in the examples should be replaced with an available model from your OpenAI account
- The web interface examples (ChatBotApp.py and SimpleUi.py) will launch a local server that you can access through your web browser

