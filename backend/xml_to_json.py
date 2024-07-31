from flask import Flask, request, jsonify
import requests
import xml.etree.ElementTree as ET
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "sk-proj-nG1chS1anW8pUY8ne8cJT3BlbkFJpyxGlhh0E3EiaxhsPiUR"

# Function to fetch data from the NSF API
def fetch_nsf_awards(keyword):
    url = f'http://api.nsf.gov/services/v1/awards.xml?keyword={keyword}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

# Function to process data with OpenAI
def process_with_openai(data, query):
    # Parse XML data
    root = ET.fromstring(data)
    awards = []
    for award in root.findall('.//award'):
        title = award.find('title').text
        abstract = award.find('abstract').text if award.find('abstract') is not None else "No abstract available"
        awards.append({"title": title, "abstract": abstract})
    
    # Combine award abstracts into a single text
    combined_abstracts = "\n".join([award["abstract"] for award in awards])

    # Prepare the OpenAI prompt
    prompt = f"{query}\n\nHere are the abstracts of the awards:\n{combined_abstracts}"

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message['content']

# Endpoint to process awards
@app.route('/process_awards', methods=['POST'])
def process_awards():
    keyword = request.json.get('keyword')
    query = request.json.get('query')

    if not keyword or not query:
        return jsonify({"error": "Keyword and query are required"}), 400

    # Fetch data from NSF API
    nsf_data = fetch_nsf_awards(keyword)
    if nsf_data is None:
        return jsonify({"error": "Failed to fetch data from NSF API"}), 500

    # Process data with OpenAI
    openai_result = process_with_openai(nsf_data, query)

    return jsonify({"result": openai_result})

if __name__ == '__main__':
    app.run(debug=True)
