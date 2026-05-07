# Timber Sales Assistant

A simple LLM-powered chatbot for a timber business. It allows users to:

- View available timber types
- Check unit prices
- Calculate total cost for purchases

The assistant uses OpenAI function calling and a local SQLite database.

---

## Tech Stack

- Python
- Gradio (UI)
- OpenAI API (LLM + tool calling)
- SQLite (local database)
- uv (environment + dependency management)


## Setup (uv) and run the application
### 1. Clone the repository
```bash
git clone https://github.com/duhirwe/llm-engineering-projects.git
cd timber-sales-assistant
```
### 2. Install dependencies
```bash
uv sync
```
This will:

create ```.venv```
install all dependencies from ```pyproject.toml```

### 3. To activate the virtual environment
- cmd : ```.venv\Scripts\activate.bat```
- macOS/Linux: ```.venv/bin/activate```

### 4. Run the application
```bash
python main.py
```
Gradio will start a local web server and provide a URL.


