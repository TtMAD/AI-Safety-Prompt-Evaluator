# AI Safety Prompt Evaluator (AISPE)

## Overview

The **AI Safety Prompt Evaluator (AISPE)** is a simple toolkit designed to assess the safety of AI language models by sending a curated set of safety-focused prompts and analyzing the responses for potential safety violations. AISPE helps developers and researchers ensure that AI models adhere to safety standards and ethical guidelines.

## Features

- **Curated Safety Prompts:** A diverse set of prompts targeting various safety aspects like bias, misinformation, and inappropriate content.
- **Automated Evaluation:** Scripts to send prompts to AI models and collect responses.
- **Response Analysis:** Simple rule-based checks to identify potential safety issues.
- **Reporting:** Generate summary reports of the findings for easy review.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- OpenAI API key

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/AI-Safety-Prompt-Evaluator.git
    cd AI-Safety-Prompt-Evaluator
    ```

2. **Set Up Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set OpenAI API Key**

    Obtain your OpenAI API key and set it as an environment variable:

    ```bash
    export OPENAI_API_KEY='your-api-key-here'  # On Windows use `set` instead of `export`
    ```

### Usage

#### 1. **Send Prompts and Collect Responses**

Navigate to the `scripts` directory and run the `send_prompts.py` script:

```bash
cd scripts
python send_prompts.py