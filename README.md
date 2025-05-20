# TikTok Search Engine with Exa API

This project is a Python-based search tool that uses the [Exa API](https://exa.ai) to search for TikTok videos by keyword. It filters results to only include content from TikTok's domain and outputs the video titles and URLs.

## Features

- Accepts search keywords from user input
- Filters web results to TikTok links only
- Secure API key management using `.env`
- Clean output of video titles and links

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Alan-Garci/exa-tiktok-search-engine.git
cd exa-tiktok-search-engine
```

### 2. Install dependencies
```bash
pip install exa-py python-dotenv
```

### 3. Add your API key
```bash
create a .env file in the root directory with:
EXA_API_KEY=your_actual_api_key_here
```

### 4. Run the script
```bash
python main.py
```

# This project is based on a tutorial from Codedex. While completing it, I learned how to:
- Work with 3rd party APIs in python
- Filter Search results with domain constraints
- Securely manage API keys using dotenv

This project is for educational purposes only
