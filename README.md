# Data Analyzer & Visualizer using AutoGen

![Python](https://img.shields.io/badge/language-python-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-orange)
![AutoGen](https://img.shields.io/badge/Framework-Agentic%20AI-green)

## Overview

This repository provides an extensible agentic AI application for automated data analysis and visualization, powered by [AutoGen](https://github.com/microsoft/autogen). It enables users to interact via natural language, upload CSV datasets, request analyses, and receive Python code and graphical outputs. The system leverages modular AI agents for collaborative data tasks, including code generation, execution, and result interpretation.

## Features

- **Modular Agent Design:**  
  - `Data_Analyzer_Agent`: Interprets user data questions and generates Python code for analysis.
  - `Code_Executor_Agent`: Safely runs the generated code, manages dependencies, and returns results/errors.
  - `Analyzer GPT Team`: Orchestrates agent interactions via round-robin GroupChat with custom termination.

- **Flexible Data Analysis:**  
  - Upload CSV files and request specific analyses or visualizations (e.g., "Show a graph of survivors in Titanic data").
  - Auto-detects and installs missing Python libraries.
  - Uses `matplotlib` for saving plots as `output.png`.

- **Streamlit Web App:**  
  - Intuitive UI for dataset upload and task submission.
  - Real-time chat interface with agent personas and result streaming.
  - Maintains conversation state for persistent analysis sessions.

- **Robust Architecture:**  
  - Clean separation of concerns: agents, teams, configuration, and utilities.
  - Scalable and maintainable project structure for multi-agent workflows.

- **Docker Integration:**  
  - All user-generated code is executed inside a Docker container for security and reproducibility.
  - Docker ensures that code execution is isolated from the host system and that all dependencies (Python packages) are installed in a controlled environment.
  - The application manages the Docker lifecycle: it starts the container before analysis and stops it afterward.
  - This allows running arbitrary Python code, installing packages with `pip`, and saves generated files (such as `output.png`) securely.

## Project Structure

```
Data_Analyzer_Visualizer_using_Autogen/
├── agents/                     # Agent definitions & prompts
│   ├── Data_analyzer_agent.py
│   ├── Code_executor_agent.py
│   └── prompts/
├── teams/                      # Agent collaboration logic
│   └── analyzer_gpt.py
├── config/                     # Model & Docker configuration
│   ├── openai_model_client.py
│   └── docker_util.py
├── utils/                      # Shared utilities (e.g., logging)
├── main.py                     # CLI entry point
├── streamlit_app.py            # Streamlit web app
├── Project Structure Guide.ipynb # Documentation & best practices
├── requirements.txt            # Python dependencies
└── LICENSE
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/UtkPatAI25/Data_Analyzer_Visualizer_using_Autogen.git
   cd Data_Analyzer_Visualizer_using_Autogen
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Copy `.env.sample` to `.env` and add your OpenAI API key and other secrets.

4. **Docker Setup:**
   - **Required:** Install [Docker](https://docs.docker.com/get-docker/) and ensure it is running.
   - The application will automatically build and start a container where all user code is executed.
   - No manual container management is needed; the app handles starting and stopping as needed.

5. **Run the CLI demo:**
   ```bash
   python main.py
   ```

6. **Launch the Streamlit app:**
   ```bash
   streamlit run streamlit_app.py
   ```
   - Upload your CSV and enter analysis tasks in chat.

## Usage

- **Upload Data:** Use the Streamlit interface to upload a CSV file.
- **Ask Questions:** Enter natural language requests (e.g., "Show a bar chart of age distribution").
- **View Results:** Agents collaborate to analyze your data, display code, output, and visualizations.

**Sample Task:**  
_"Can you give me a graph of survived and died in my data titanic.csv and save it as output.png?"_

## Docker Security & Workflow

- All Python code written by the agents is run inside a Docker container.
- If your task requires new Python libraries (like `pandas` or `matplotlib`), the agent will instruct to install them with `pip install ...` inside Docker.
- Execution results, errors, or generated output files (such as images) are captured from the container and presented in the UI.
- The container is stopped after the analysis, ensuring no lingering processes.
- This approach keeps your host environment secure and clean, regardless of what code is generated or run.

## Agent Workflow

1. **User Request:** Task submitted via chat or CLI.
2. **Data_Analyzer_Agent:** Plans the analysis, generates Python code (with explanations).
3. **Code_Executor_Agent:** Executes code, installs missing libraries in Docker, returns output/errors.
4. **Team Orchestration:** Agents collaborate until termination condition (`STOP`) is met.
5. **Result Delivery:** Outputs (including images) are saved and presented to the user.

## Best Practices & Customization

- Follow the modular architecture for adding new agents or analysis types.
- Refer to `Project Structure Guide.ipynb` for organization, testing, and production readiness tips.
- Customize prompts and agent behaviors for targeted use-cases.

## License

This project is licensed under the MIT License.

---

**Maintainer:** [UtkPatAI25](https://github.com/UtkPatAI25)  
**Contributions and feedback welcome!**
