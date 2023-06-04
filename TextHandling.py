import openai
import textwrap
import concurrent.futures
from youtube_transcript_api import YouTubeTranscriptApi
import urllib

# Replace 'your_api_key_here' with your actual API key
# In the future, use parallelization to compute all the components at once to make it quicker.


def break_up_text(text, max_length):
    return textwrap.wrap(text, max_length)


def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    


api_file = "api_key.txt"
openai.api_key = read_text_from_file(api_file)

def summarize_part(part):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role": "system", "content": "Summarize this text into a markdown file for concise notes. Make a title and headers for each section of the text. Keep the timestamps for key parts."},
            {"role": "user", "content": part }
        ]
    )

    summary = response['choices'][0]['message']['content']
    return summary


def generate_transcript(id):
	transcript = YouTubeTranscriptApi.get_transcript(id)
	script = ""

	for text in transcript:
		t = text["text"]
		if t != '[Music]':
			script += t + " "
		
	return script



def gpt_4_summarize(input_file, output_file, max_length=14000):
    id = input('Enter Video Link:')
    print(id)
    text = generate_transcript(id)
    broken_text = break_up_text(text, max_length)
    summaries = []
    
    print("Parts:\t" + str(len(broken_text)))

    # Use a ThreadPoolExecutor to parallelize the task
    with concurrent.futures.ThreadPoolExecutor() as executor:
        summaries = list(executor.map(summarize_part, broken_text))

    summaries = "".join(summaries)

    with open(output_file, 'w') as file:
        file.write(summaries)

    return summaries

# Example usage
input_file = "input.txt"
output_file = "Lectures/Color Theory.md"

markdown_summary = gpt_4_summarize(input_file, output_file)
# print(markdown_summary)
