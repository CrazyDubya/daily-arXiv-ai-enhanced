# About
This tool will daily crawl https://arxiv.org and use LLMs to summarize them.

See in: https://dw-dengwei.github.io/daily-arXiv-ai-enhanced/

# How to use
This repo will daily crawl arXiv papers about **cs.CV, cs.GR and cs.CL**, and use **OpenAI** or **Ollama** to summarize the papers in **Chinese**.
If you wish to crawl other arXiv categories, use other LLMs or other languages, please follow the instructions below.
Otherwise, you can directly use this repo in https://dw-dengwei.github.io/daily-arXiv-ai-enhanced/ . Please star it if you like :)

## Setup Instructions

### Option 1: Using OpenAI (Default)
1. Fork this repo to your own account
2. Go to: your-own-repo -> Settings -> Secrets and variables -> Actions
3. Go to Secrets. Secrets are encrypted and are used for sensitive data
4. Create two repository secrets named `OPENAI_API_KEY` and `OPENAI_BASE_URL`, and input corresponding values.
5. Go to Variables. Variables are shown as plain text and are used for non-sensitive data
6. Create the following repository variables:
   1. `AI_PROVIDER`: "openai" (optional, this is the default)
   2. `CATEGORIES`: separate the categories with ",", such as "cs.CL, cs.CV"
   3. `LANGUAGE`: such as "Chinese" or "English"
   4. `MODEL_NAME`: such as "gpt-4o-mini" or "deepseek-chat"
   5. `EMAIL`: your email for push to github
   6. `NAME`: your name for push to github

### Option 2: Using Ollama (Local/Self-hosted)
1. Fork this repo to your own account
2. Set up Ollama service (locally or on a server accessible to GitHub Actions)
3. Go to: your-own-repo -> Settings -> Secrets and variables -> Actions -> Variables
4. Create the following repository variables:
   1. `AI_PROVIDER`: "ollama"
   2. `OLLAMA_BASE_URL`: such as "http://localhost:11434" or "http://your-ollama-server:11434"
   3. `OLLAMA_MODEL`: such as "llama3.2", "mistral", or "codellama"
   4. `CATEGORIES`: separate the categories with ",", such as "cs.CL, cs.CV"
   5. `LANGUAGE`: such as "Chinese" or "English"
   6. `EMAIL`: your email for push to github
   7. `NAME`: your name for push to github

### Running the Workflow
7. Go to your-own-repo -> Actions -> arXiv-daily-ai-enhanced
8. You can manually click **Run workflow** to test if it works well (it may takes about one hour). 
By default, this action will automatically run every day
You can modify it in `.github/workflows/run.yml`
9. If you wish to modify the content in `README.md`, do not directly edit README.md. You should edit `template.md`.

## Environment Variables Reference

### AI Provider Configuration
- `AI_PROVIDER`: Choose between "openai" (default) or "ollama"

### OpenAI Configuration
- `OPENAI_API_KEY`: Your OpenAI API key (required for OpenAI provider)
- `OPENAI_BASE_URL`: OpenAI API base URL (optional, defaults to "https://api.openai.com/v1")
- `MODEL_NAME`: OpenAI model name like "gpt-4o-mini", "gpt-4", "deepseek-chat"

### Ollama Configuration  
- `OLLAMA_BASE_URL`: Ollama service URL (optional, defaults to "http://localhost:11434")
- `OLLAMA_MODEL`: Ollama model name like "llama3.2", "mistral", "codellama"

### General Configuration
- `LANGUAGE`: Output language like "Chinese" or "English"  
- `CATEGORIES`: arXiv categories like "cs.CL, cs.CV"
- `EMAIL`: Your email for git commits
- `NAME`: Your name for git commits

### Local Development
For local development, you can set these as environment variables or create a `.env` file in the project root.

# To-do list
- [x] Replace markdown with GitHub pages front-end.
- [ ] Bugfix: In the statistics page, the number of papers for a keyword is not correct.
- [ ] Update instructions for fork users about how to use github pages.

# Content
{readme_content}

# Related tools
- ICML, ICLR, NeurIPS list: https://dw-dengwei.github.io/OpenReview-paper-list/index.html

# Star history

[![Star History Chart](https://api.star-history.com/svg?repos=dw-dengwei/daily-arXiv-ai-enhanced&type=Date)](https://www.star-history.com/#dw-dengwei/daily-arXiv-ai-enhanced&Date)
