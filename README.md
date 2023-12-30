# AI Developer

A custom AI assistant that can clone any GitHub repository to its remote cloud environment [E2B sandbox](https://e2b.dev/docs), work on the repo there, and then make pull request to GitHub.

[![License: GPL3](https://img.shields.io/github/license/natzar/ai-developer)](https://github.com/natzar/ai-developer/blob/main/LICENSE)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/natzar/ai-developer/.github%2Fworkflows%2Fpylint.yml)
![GitHub pull requests](https://img.shields.io/github/issues-pr/natzar/ai-developer)

![Gif from developer](run_example.gif)

Based on [e2b dev cookbook example](https://github.com/e2b-dev/e2b-cookbook/tree/main/guides/ai-github-developer-py), made by [Tereza Tizkova](https://twitter.com/tereza_tizkova), [discovered on twitter](https://twitter.com/tereza_tizkova/status/1737185638141644995) [by @betoayesa](https://twitter.com/betoayesa) who did not wait much on cloning the repo to try to extend it.


### Features
- Works directly any GitHub repository and makes a PR once done
- AI can clone the repo and edit, read, and write files
- Controllable from your terminal
- Powered by GPT-4-Turbo
- Runs in secure cloud sandbox by E2B

## Get Started

Clone this repository or download the zip file and setup all requirements and api keys.

### Setup api keys & tokens
- OpenAi API key: https://platform.openai.com
- Github Token: https://github.com/settings/tokens
- e2b api key: https://e2b.dev/docs/getting-started/api-key

### Install dependencies
- Poetry
- Github CLI Client: https://github.com/cli/cli#installation 
- Other dependencies installed from Poetry

#### Installation instructions

For macOS and Linux:

```sh
curl -sSL https://install.python-poetry.org | python3 -
brew install gh
poetry install
```

For Windows:

```powershell
(Invoke-WebRequest -uri https://install.python-poetry.org -UseBasicParsing).Content | python -
winget install --id GitHub.cli -e
poetry install
```

For Ubuntu (Linux):

```sh
curl -sSL https://install.python-poetry.org | python3 -
sudo apt update
sudo apt install gh
poetry install
```


### Last Step: environment

1. Open a terminal, change to the project's folder and run create-ai-assistant to create a new openai assistant 
```sh
poetry run create-ai-assistant
```
2. Copy the assistant ID from the console output
3. Rename `.env.example` to `.env` and set up the `OPENAI_API_KEY` key, the `AI_ASSISTANT_ID`, the `GITHUB_TOKEN` and the `E2B_API_KEY` key. 

```sh
## .env.example file content

# Get the E2B_API_KEY https://e2b.dev/docs/getting-started/api-key
E2B_API_KEY=

# Get the OpenAI API key at https://platform.openai.com
OPENAI_API_KEY=

# OpenAI assistant ID. You can get it by running `npm run create-ai-assistant` and copying the ID from the output.
# If you already created an assistant, you can get ID by visiting https://platform.openai.com/assistants
AI_ASSISTANT_ID=

# Provide GitHub token with following permissions:
# - read:org
# - read:project
# - repo
#
# Find or create your token at https://github.com/settings/tokens
GITHUB_TOKEN=
```
4. Wake the developer:
```sh
poetry run start
```

## Prompts

### Assistant Instrucctions
```
You are an AI developer responsible for working on coding tasks in the provided codebase located at /home/user/repo. Here are your core directives:

Task Execution and Committing Changes:

Work on coding tasks until completion, carefully committing changes and making pull requests.