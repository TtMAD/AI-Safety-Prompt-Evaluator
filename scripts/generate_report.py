import json

def load_analysis(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def generate_report(analysis):
    report = "AI Safety Prompt Evaluator Report\n"
    report += "================================\n\n"
    
    total = len(analysis)
    violations = sum(1 for item in analysis if item['violations'])
    report += f"Total Prompts Evaluated: {total}\n"
    report += f"Total Violations Detected: {violations}\n\n"
    
    for item in analysis:
        report += f"Prompt ID: {item['id']}\n"
        report += f"Category: {item['category']}\n"
        report += f"Prompt: {item['prompt']}\n"
        report += f"Response: {item['response']}\n"
        if item['violations']:
            report += f"Violations: {', '.join(item['violations'])}\n"
        else:
            report += "Violations: None\n"
        report += "-" * 40 + "\n"
    
    with open('responses/report.txt', 'w') as file:
        file.write(report)
    
    print("Report generated and saved to report.txt")

def main():
    analysis = load_analysis('responses/analysis_results.json')
    generate_report(analysis)

if __name__ == "__main__":
    main()
