# 🚀 Day 2: Build AI Agents with YAML (Zero Code)

[![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://google.github.io/adk-docs/)
[![Gemini](https://img.shields.io/badge/Gemini-2.0-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache_2.0-green?style=for-the-badge)](LICENSE)

> **Part of Google's Advent of Agents Series**
> 
> Build your first AI agent with Gemini in under 5 minutes — without writing a single line of code.

```
4 lines of YAML = 1 working AI agent
```

## 📖 Table of Contents

- [Overview](#-overview)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Hello World Examples](#-hello-world-examples)
  - [Example 1: Basic Agent (4 Lines)](#example-1-basic-agent-4-lines)
  - [Example 2: Search Agent (Built-in Tools)](#example-2-search-agent-built-in-tools)
  - [Example 3: Custom Tools Agent](#example-3-custom-tools-agent)
- [Multi-Agent System](#-multi-agent-system-bonus)
- [Project Structure](#-project-structure)
- [Configuration Reference](#-configuration-reference)
- [Deployment](#-deployment)
- [Troubleshooting](#-troubleshooting)
- [Resources](#-resources)

## 🎯 Overview

### What You'll Learn

| Concept | Description |
|---------|-------------|
| **Agent Config** | Define agents using YAML instead of Python code |
| **Built-in Tools** | Use google_search, code_execution out of the box |
| **Custom Tools** | Add Python functions when you need more power |
| **Sub-Agents** | Build multi-agent systems with delegation |

### Why YAML Agents?

- ✅ **No coding required** — Perfect for prototyping and non-developers
- ✅ **Production-ready** — Same capabilities as Python agents
- ✅ **Scalable** — Start simple, add complexity when needed
- ✅ **Deployable** — Works with Cloud Run and Agent Engine

## 📋 Prerequisites

### Required

- Python 3.10 or higher
- Google API Key (Gemini) or Google Cloud Project

### Installation

```bash
# Install Google ADK
pip install google-adk

# Verify installation
adk --version
```

### Get Your API Key

**Option A: Google AI Studio (Recommended for beginners)**
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your key

**Option B: Google Cloud (For production)**
1. Create a [Google Cloud Project](https://console.cloud.google.com)
2. Enable the Vertex AI API
3. Set up authentication

---

## ⚡ Quick Start

```bash
# Create a new agent project
adk create --type=config my_first_agent

# Add your API key to .env file
echo "GOOGLE_API_KEY=your-api-key-here" > .env

# Run the agent with web UI
adk web 
```

Open http://localhost:8000 and start chatting with your agent!

## 🌍 Hello World Examples

### Example 1: Basic Agent (4 Lines)

> **The simplest possible agent — just 4 lines of YAML**

#### File Structure

```
hello_basic/
├── .env
└── root_agent.yaml
```

#### `.env`

```env
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=your-api-key-here
```

#### `root_agent.yaml`

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/google/adk-python/refs/heads/main/src/google/adk/agents/config_schemas/AgentConfig.json
name: hello_agent
model: gemini-2.0-flash
description: A friendly assistant that greets users.
instruction: You are a friendly assistant. Greet users warmly and help answer their questions.
```

#### Run It

```bash
adk web 
```

#### What's Happening?

| Line | Purpose |
|------|---------|
| `name` | Unique identifier for your agent |
| `model` | The Gemini model powering your agent |
| `description` | What your agent does (used by orchestrators) |
| `instruction` | System prompt defining agent behavior |

### Example 2: Search Agent (Built-in Tools)

> **Add Google Search capability with just 2 extra lines**

#### File Structure

```
hello_search/
├── .env
└── root_agent.yaml
```

#### `root_agent.yaml`

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/google/adk-python/refs/heads/main/src/google/adk/agents/config_schemas/AgentConfig.json
name: search_assistant
model: gemini-2.0-flash
description: An assistant that searches the web to answer questions with current information.
instruction: |
  You are a helpful research assistant with access to Google Search.
  
  When users ask questions:
  1. Use google_search to find current, accurate information
  2. Summarize findings in a clear, concise way
  3. Always cite your sources
  
  Be helpful, accurate, and conversational.

tools:
  - name: google_search
```

#### Run It

```bash
cd hello_search
adk web 
```

#### Test Prompts

- "What's the latest news about AI agents?"
- "Who won the most recent Champions League match?"
- "What's the current price of Bitcoin?"

#### Available Built-in Tools

| Tool | Description |
|------|-------------|
| `google_search` | Search the web for current information |
| `code_execution` | Execute Python code in a sandbox |
| `load_artifacts` | Load files and documents |
| `url_context` | Fetch and analyze web pages |

### Example 3: Custom Tools Agent

> **Add your own Python functions as tools**

#### File Structure

```
hello_custom/
├── .env
├── root_agent.yaml
└── tools.py
```

#### `root_agent.yaml`

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/google/adk-python/refs/heads/main/src/google/adk/agents/config_schemas/AgentConfig.json
name: calculator_agent
model: gemini-2.0-flash
description: A math assistant that can perform calculations and check prime numbers.
instruction: |
  You are a helpful math assistant with calculator tools.
  
  When users ask math questions:
  1. Use the calculate tool for arithmetic operations
  2. Use is_prime to check if numbers are prime
  3. Explain your reasoning step by step
  4. Never calculate manually - always use the tools
  
  Be educational and help users understand the math.

tools:
  - name: tools.calculate
  - name: tools.is_prime
```

#### `tools.py`

```python
"""Custom tools for the calculator agent."""

import math
from typing import Union


def calculate(expression: str) -> dict:
    """
    Evaluate a mathematical expression safely.
    
    Args:
        expression: A math expression like "2 + 2" or "sqrt(16) * 3"
    
    Returns:
        dict with 'result' or 'error' key
    
    Examples:
        calculate("2 + 2") -> {"result": 4, "expression": "2 + 2"}
        calculate("sqrt(16)") -> {"result": 4.0, "expression": "sqrt(16)"}
    """
    # Define safe mathematical functions
    safe_functions = {
        # Basic operations
        'abs': abs,
        'round': round,
        'min': min,
        'max': max,
        'sum': sum,
        'pow': pow,
        
        # Math module functions
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'log': math.log,
        'log10': math.log10,
        'log2': math.log2,
        'exp': math.exp,
        'floor': math.floor,
        'ceil': math.ceil,
        
        # Constants
        'pi': math.pi,
        'e': math.e,
    }
    
    try:
        # Safely evaluate the expression
        result = eval(expression, {"__builtins__": {}}, safe_functions)
        return {
            "success": True,
            "result": result,
            "expression": expression
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "expression": expression
        }


def is_prime(numbers: list[int]) -> dict:
    """
    Check if numbers are prime.
    
    Args:
        numbers: List of integers to check
    
    Returns:
        dict with results for each number and list of primes
    
    Examples:
        is_prime([2, 3, 4, 5]) -> {
            "results": {2: True, 3: True, 4: False, 5: True},
            "primes": [2, 3, 5],
            "not_primes": [4]
        }
    """
    def check_prime(n: int) -> bool:
        """Check if a single number is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    results = {num: check_prime(num) for num in numbers}
    
    return {
        "results": results,
        "primes": [num for num, is_p in results.items() if is_p],
        "not_primes": [num for num, is_p in results.items() if not is_p],
        "count": {
            "total": len(numbers),
            "primes": sum(1 for is_p in results.values() if is_p),
            "not_primes": sum(1 for is_p in results.values() if not is_p)
        }
    }


def factorial(n: int) -> dict:
    """
    Calculate the factorial of a number.
    
    Args:
        n: Non-negative integer
    
    Returns:
        dict with factorial result
    """
    if n < 0:
        return {"success": False, "error": "Factorial not defined for negative numbers"}
    if n > 170:
        return {"success": False, "error": "Number too large (max 170)"}
    
    return {
        "success": True,
        "n": n,
        "factorial": math.factorial(n)
    }


def fibonacci(n: int) -> dict:
    """
    Generate Fibonacci sequence up to n terms.
    
    Args:
        n: Number of terms to generate
    
    Returns:
        dict with Fibonacci sequence
    """
    if n <= 0:
        return {"success": False, "error": "n must be positive"}
    if n > 100:
        return {"success": False, "error": "n too large (max 100)"}
    
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return {
        "success": True,
        "n": n,
        "sequence": sequence,
        "sum": sum(sequence)
    }
```

#### Run It

```bash
adk web
```

#### Test Prompts

- "What is 15 * 24 + sqrt(144)?"
- "Are these numbers prime: 17, 24, 31, 100, 97?"
- "Generate the first 15 Fibonacci numbers"


## 🤖 Multi-Agent System (Bonus)

> **Build a team of specialized agents that work together**

#### File Structure

```
multi_agent/
├── .env
├── root_agent.yaml
├── researcher_agent.yaml
├── writer_agent.yaml
└── tools.py
```

#### `root_agent.yaml` (Orchestrator)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/google/adk-python/refs/heads/main/src/google/adk/agents/config_schemas/AgentConfig.json
name: orchestrator
model: gemini-2.0-flash
description: Coordinates research and writing tasks between specialized agents.
instruction: |
  You are an orchestrator agent that coordinates work between specialized agents.
  
  Your team:
  - researcher_agent: Searches for information and gathers facts
  - writer_agent: Creates polished content from research
  
  Workflow:
  1. Analyze the user's request
  2. If research is needed, delegate to researcher_agent first
  3. For content creation, send research to writer_agent
  4. Synthesize and present final results to user
  
  Always explain what each agent is doing.

sub_agents:
  - config_path: researcher_agent.yaml
  - config_path: writer_agent.yaml
```

#### `researcher_agent.yaml`

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/google/adk-python/refs/heads/main/src/google/adk/agents/config_schemas/AgentConfig.json
name: researcher_agent
model: gemini-2.0-flash
description: Searches the web and gathers information on topics.
instruction: |
  You are a research specialist with access to Google Search.
  
  Your responsibilities:
  1. Search for accurate, current information
  2. Verify facts from multiple sources when possible
  3. Organize findings in a structured format
  4. Include source URLs for citations
  
  Return comprehensive research summaries to the orchestrator.

tools:
  - name: google_search
```

#### `writer_agent.yaml`

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/google/adk-python/refs/heads/main/src/google/adk/agents/config_schemas/AgentConfig.json
name: writer_agent
model: gemini-2.0-flash
description: Creates polished written content from research and outlines.
instruction: |
  You are a professional content writer.
  
  Your responsibilities:
  1. Transform research into engaging content
  2. Adapt tone and style to the content type (blog, report, social media)
  3. Ensure clarity and readability
  4. Properly attribute sources
  
  Content types you can create:
  - Blog posts
  - Executive summaries
  - Social media posts
  - Technical documentation
  - Email drafts

tools:
  - name: tools.format_content
```

#### `tools.py`

```python
"""Tools for the multi-agent system."""

def format_content(content: str, format_type: str = "markdown") -> dict:
    """
    Format content for different output types.
    
    Args:
        content: The content to format
        format_type: One of 'markdown', 'html', 'plain', 'social'
    
    Returns:
        Formatted content
    """
    if format_type == "social":
        # Truncate for social media
        if len(content) > 280:
            content = content[:277] + "..."
        return {
            "format": "social",
            "content": content,
            "character_count": len(content)
        }
    
    elif format_type == "html":
        # Basic markdown to HTML conversion
        html = content.replace("\n\n", "</p><p>")
        html = f"<p>{html}</p>"
        return {
            "format": "html",
            "content": html
        }
    
    return {
        "format": format_type,
        "content": content
    }
```

#### Run It

```bash
cd multi_agent
adk web .
```

#### Test Prompts

- "Research the latest developments in AI agents and write a blog post about it"
- "Find information about renewable energy trends and create an executive summary"
- "Research Google ADK and write a Twitter thread about its features"

## 📚 Configuration Reference

### Agent Config Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | ✅ | Unique identifier for the agent |
| `model` | ✅ | Gemini model to use |
| `description` | ✅ | What the agent does |
| `instruction` | ✅ | System prompt / behavior |
| `tools` | ❌ | List of tools the agent can use |
| `sub_agents` | ❌ | List of sub-agents for delegation |
| `agent_class` | ❌ | Agent type (default: LlmAgent) |

### Supported Models

| Model | Best For |
|-------|----------|
| `gemini-2.0-flash` | Fast responses, general tasks |
| `gemini-2.5-flash` | Balanced performance |
| `gemini-2.5-pro` | Complex reasoning tasks |

### Built-in Tools

| Tool | Description |
|------|-------------|
| `google_search` | Web search |
| `code_execution` | Run Python code |
| `load_artifacts` | Load files |
| `url_context` | Fetch web pages |
| `exit_loop` | Exit workflow loops |

## 🚀 Deployment

### Deploy to Cloud Run

```bash
# Build container
gcloud builds submit --tag gcr.io/PROJECT_ID/my-agent

# Deploy
gcloud run deploy my-agent \
  --image gcr.io/PROJECT_ID/my-agent \
  --platform managed \
  --allow-unauthenticated
```

### Deploy to Agent Engine

```bash
# Package your agent
adk deploy agent-engine \
  --project=PROJECT_ID \
  --location=us-central1
```

## 🔧 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `adk: command not found` | Run `pip install google-adk` and ensure PATH is set |
| `API key invalid` | Check `.env` file and regenerate key if needed |
| `Model not found` | Verify model name (e.g., `gemini-2.0-flash`) |
| `Tool not found` | Check tool path matches file/function name |

## 📚 Resources

### Official Documentation

- [Google ADK Docs](https://google.github.io/adk-docs/)
- [Agent Config Reference](https://google.github.io/adk-docs/api-reference/agentconfig/)
- [ADK Python GitHub](https://github.com/google/adk-python)

### Sample Repositories

- [ADK Samples](https://github.com/google/adk-python/tree/main/contributing/samples)

### Community

- [LinkedIn Community](https://linkedin.com/groups/genaiguru)

## 📊 Comparison Chart

| Feature | Hello World #1 | Hello World #2 | Hello World #3 | Multi-Agent |
|---------|---------------|----------------|----------------|-------------|
| **YAML Lines** | 4 | 12 | 18 | 40+ |
| **Python Code** | ❌ | ❌ | ✅ | ✅ |
| **Tools** | None | google_search | Custom | Mixed |
| **Sub-Agents** | ❌ | ❌ | ❌ | ✅ |
| **Difficulty** | Beginner | Beginner | Intermediate | Advanced |
| **Use Case** | Simple Q&A | Research | Calculations | Complex workflows |

## 🎬 What's Next?

**Day 3 Preview:** Multi-Agent Orchestration Patterns
- Sequential workflows
- Parallel execution
- Loop agents
- Agent-to-Agent communication

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

<div align="center">

**Built with ❤️ for the Google Advent of Agents Series**

[⭐ Star this repo](https://github.com/user/adk-agent-config) · [🐛 Report Bug](https://github.com/user/adk-agent-config/issues) · [💡 Request Feature](https://github.com/user/adk-agent-config/issues)

</div>
