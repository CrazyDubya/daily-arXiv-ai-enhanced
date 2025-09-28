# Local Development Guide

This guide helps you set up and test the daily-arXiv-ai-enhanced project locally.

## Quick Setup

### 1. Install Dependencies

Using pip (if uv is not available):
```bash
pip3 install arxiv python-dotenv langchain langchain-openai scrapy tqdm
```

Using uv (recommended for production):

> **Security Note:**  
> Piping remote scripts directly to the shell is a security risk.  
> Before running the following command, you should review the script at [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) to ensure it is safe.  
>  
> **Alternative installation (recommended):**  
> If you have [pipx](https://pypa.github.io/pipx/) installed, you can install uv safely with:  
> ```bash
> pipx install uv
> ```
> Or, using pip (not as isolated):  
> ```bash
> pip install uv
> ```
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
```

### 2. Test the Setup

Run the validation script:
```bash
python3 scripts/test_setup.py
```

### 3. Test Web Interface Locally

Start a local web server:
```bash
python3 -m http.server 8080
```

Then open http://localhost:8080 in your browser.

## Development Workflow

### Testing Data Processing

The system has existing sample data in the `data/` directory that you can use for testing:

1. **Markdown Conversion**: Convert AI-enhanced data to markdown
```bash
cd to_md
python3 convert.py --data ../data/2025-08-01_AI_enhanced_Chinese.jsonl
```

2. **README Generation**: Update README from template
```bash
python3 update_readme.py
```

### Local Testing Without API

For testing the crawling and processing pipeline without requiring OpenAI API keys:

```bash
# Run partial workflow (crawling + deduplication only)
./run.sh
# Choose 'y' when prompted for partial workflow
```

## Full Production Setup

For complete functionality with AI enhancement, you need:

1. **Environment Variables** (for GitHub Actions or full local testing):
   - `OPENAI_API_KEY`: Your OpenAI-compatible API key
   - `OPENAI_BASE_URL`: API endpoint (default: https://api.openai.com/v1)
   - `LANGUAGE`: Target language (default: Chinese)
   - `CATEGORIES`: arXiv categories (default: cs.CV, cs.CL)
   - `MODEL_NAME`: LLM model name (default: gpt-4o-mini)

2. **GitHub Repository Setup**:
   - Fork the repository
   - Set up repository secrets and variables in GitHub
   - Enable GitHub Pages
   - Configure the daily workflow

## Project Structure

```
├── data/                     # Generated papers data (JSON + Markdown)
├── daily_arxiv/             # Scrapy spider for arXiv crawling
├── ai/                      # AI enhancement scripts
├── to_md/                   # Markdown conversion
├── js/, css/                # Web interface assets
├── index.html               # Main paper listing page
├── settings.html            # User preferences page
├── statistic.html           # Statistics and trends page
├── run.sh                   # Local testing script
├── update_readme.py         # README generation
└── template.md              # README template
```

## Troubleshooting

### Common Issues

1. **External resources blocked**: When running locally, external CDN resources (fonts, flatpickr) may be blocked. This is expected and doesn't affect core functionality.

2. **No AI-enhanced data**: If you only have basic `.jsonl` files without AI enhancement, you can still test the web interface with the existing enhanced data files.

3. **Permission errors**: Make sure `run.sh` is executable: `chmod +x run.sh`

### Validation

Use the test script to verify your setup:
```bash
python3 scripts/test_setup.py
```

This checks:
- ✅ Data file structure and content
- ✅ Markdown conversion functionality  
- ✅ README generation system
- ✅ Web assets availability