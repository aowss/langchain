# Build a simple LLM application

This follows [this tutorial](https://www.langchain.com/).

Steps:

1. Sign up to [LangSmith](https://smith.langchain.com/)

2. Create a `.env` file with the environment variables

```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="..."
LANGCHAIN_PROJECT="..."
```

3. Sign up to [OpenAI](https://openai.com) and [create an API key](https://platform.openai.com/api-keys)

Add that API key to the previously created `.env` file with a key of `OPENAI_API_KEY` 