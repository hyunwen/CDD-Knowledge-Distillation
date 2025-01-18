from google import genai
from datasets import load_dataset
import re
import os
import json

# Configure the API key
client = genai.Client(api_key='AIzaSyBW-dfrlDexjkq224Y9X8j-dAvPZemourY', http_options={'api_version':'v1alpha'})

# Load the dataset
test_set = load_dataset("parquet", data_files="test-00000-of-00001.parquet")

# Open a file to save the results in JSON format
file = open('./answer.json', 'w+')

idx = 0
for i in test_set['train']:
    # Construct the prompt
    prompt = 'You are an expert in C/C++ language vulnerability detection. You focus on those vulnerabilities that can cause harm. Please analyze the following code step by step to see if there is a vulnerability, and give the analysis process. Finally, end with "The code has a vulnerability" or "The code does not have a vulnerability"' + "\nfunc:" + i['func']


    print(idx)

    try:
        # Generate the response
        response = client.models.generate_content(model='gemini-2.0-flash-thinking-exp', contents = prompt)

        thinking = "Not available"
        response_text = "Not available"

        # Iterate through parts to identify thinking and response
        
        for part in response.candidates[0].content.parts:
            #there is no `thought` attribute in part
            #so we need to distinguish thinking and response by ourself
            #if the part contains the regular expression, it is the response
            if part.thought == True:
                thinking = part.text
                print(thinking)
            #otherwise, it is the thinking
            else:
                response_text = part.text
                print(response_text)

        # Extract the answer using regular expression
        label_match = re.search(r'The code has a vulnerability|The code does not have a vulnerability', response_text)
        label = label_match.group(0) if label_match else "undefined"
        print(label)
        # Create a dictionary to store the results
        result = {
            'idx': idx,
            'thinking': thinking,
            'response': response_text,
            'label': label
        }

        # Write the result to the JSON file
        json.dump(result, file)
        file.write('\n')  # Add a newline for better readability

    except Exception as e:
        print(f"An error occurred: {e}")
        # Store an error indicator in the JSON file
        result = {
            'idx': idx,
            'thinking': "Error",
            'response': "Error",
            'label': "Error"
        }
        json.dump(result, file)
        file.write('\n')
    idx = idx + 1
file.close()