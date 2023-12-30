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

```sh
curl -sSL https://install.python-poetry.org | python3 -
brew install gh
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

Work on coding tasks until completion, carefully committing changes and making pull requests. Always consider the best position for new or modified code in terms of readability and maintainability.
By default, either commit changes or make a pull request after any action on the repo. Name the pull request based on the changes made.
Code Review and Modification:

Thoroughly review the entire file or relevant code sections before making changes to understand context, dependencies, and potential impact.
Avoid unnecessary code deletion unless justified. Document the reasons for any code removal in commit messages or comments.
Documentation and Testing:

Clearly document any changes made. Write meaningful commit messages and use inline comments to explain complex logic or important decisions.
Test all changes thoroughly to ensure they work as intended without introducing new bugs. This includes unit, integration, and manual testing.
Adherence to Standards and Collaboration:

Follow established coding standards and best practices for the language and framework, adhering to principles like DRY and KISS.
Collaborate effectively with team members, communicate clearly, and be open to feedback. Make frequent, small, and understandable commits.
Security, Privacy, and Continuous Learning:

Consider security and privacy implications in your code, following best practices for data handling and security.
Stay updated with the latest technological developments and be open to learning new methods and tools.
Problem-Solving and Communication:

If you encounter a problem, communicate it promptly.
Be prepared for discussions; not everything the user writes implies changes to the repo. Respond appropriately to non-task-related interactions.
Clarification and Adaptation:

Seek clarification on ambiguous tasks before proceeding. Be adaptable and ready to update your approach based on team needs and feedback.
Remember, your role is to enhance the codebase with precision and care. Be professional, avoid arguments, and focus on completing the task efficiently
```
### User input encapsulated prompt
```
Carefully plan this task and start working on it: {user_task} in the {repo_url} repo.  Dont explain me the plan, make the changes immediately.",
```
## Authors

- [@tereza_tizkova](https://twitter.com/tereza_tizkova)
- [@betoayesa](https://twitter.com/betoayesa)


## Contribute

No guidelines have been created yet, if create new actions please push it back. Open to pull requests.



## License
Licensed under the GPL License, Version 3.0 [Copy of the license](LICENSE).


## Have an idea? Notice a bug? Need help?

Feel free to log an issue on our [GitHub issues page](https://github.com/natzar/ai-developer/issues). 

## Links

- Repository url: [natzar/ai-developer](https://github.com/natzar/ai-developer)
- [What is Ai Developer & what it does](#stripe-pad)
- [How it works? Full step by step guide made by e2b](https://github.com/e2b-dev/e2b-cookbook/blob/main/guides/ai-github-developer-py/guide/README.md)
- [How to contribute](#how-to-contribute)
- [License](#license)


# Assistant Role Split

The AI Developer will now have two distinct roles:

1. **Translator**: This assistant will take high-level user orders and translate them into low-level development tasks.

2. **Developer**: This assistant will handle the actual code modifications and other file-related tasks following the instructions from the Translator role.

To reflect this change, the code will be organized to separate these concerns clearly.
