import json
import openai
import os
import time

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_prompts(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def send_prompt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    prompts = load_prompts('prompts/safety_prompts.json')
    responses = []
    
    for item in prompts:
        print(f"Sending Prompt ID {item['id']} - Category: {item['category']}")
        ai_response = send_prompt(item['prompt'])
        responses.append({
            "id": item['id'],
            "category": item['category'],
            "prompt": item['prompt'],
            "response": ai_response
        })
        print(f"Response: {ai_response}\n")
        time.sleep(1)  # To respect API rate limits
    
    # Save responses to a JSON file
    with open('responses/responses.json', 'w') as outfile:
        json.dump(responses, outfile, indent=4)
    
    print("All prompts have been processed and responses saved.")

if __name__ == "__main__":
    main()
