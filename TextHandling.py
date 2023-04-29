import openai
import textwrap

# Replace 'your_api_key_here' with your actual API key


def break_up_text(text, max_length):
    return textwrap.wrap(text, max_length)

def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

api_file = "api_key.txt"
openai.api_key = read_text_from_file(api_file)

def gpt_4_summarize(input_file, output_file, max_length=14000):
    text = read_text_from_file(input_file)
    broken_text = break_up_text(text, max_length)
    summaries = []
    i = 0
    print("Parts:\t" + (str)(len(broken_text)))
    for part in broken_text:
        i = i+1
        print(i)
        response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role": "system", "content": "Summarize this text into a markdown file for concise notes. Make a title and headers for each section of the text. Keep the timestamps for key parts."},
            {"role": "user", "content": part }
        ]
        )

        summary = response['choices'][0]['message']['content']
        summaries.append(summary)
    summaries = "".join(summaries)

    with open(output_file, 'w') as file:
        file.write(summaries)

    return summaries

# Example usage
input_file = "input.txt"
output_file = "summary.md"

markdown_summary = gpt_4_summarize(input_file, output_file)
# print(markdown_summary)
