import ollama

response = ollama.chat(
    model='llama3',
    messages=[
        {'role': 'user', 'content': 'What is the weather like in Derry, Northern Ireland?'}
    ]
)

print(response['message']['content'])