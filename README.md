# Dev Crew Intro

Welcome to the Dev Crew project. This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. My goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities. This crew consist of 2 agents code_write which is a junior developer and code_reviewer which a senior developer. Both have their own goals to accomplish.

# Flow of Crew
Flow starts with a problem statement, which is solved by a junior developer (code_writer agent) then the flow moves towards the senior developer (code_reviewer agent). Code reviewer agent will review and optimize the code written by junior developer and return finalized code.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` or `GEMINI_API_KEY` into the `.env` file**

- Modify `src/devflow/config/agents.yaml` to define your agents
- Modify `src/devflow/config/tasks.yaml` to define your tasks
- Modify `src/devflow/crew.py` to add your own logic, tools and specific args
- Modify `src/devflow/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
uv run kickoff
```

This command initializes the devFlow Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Understanding Your Crew

The devFlow Crew is composed of multiple AI agents, each with unique roles, goals. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Dev Crew.

Let's create wonders together with the power and simplicity of crewAI.
