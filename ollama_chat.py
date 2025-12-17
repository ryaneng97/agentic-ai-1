import ollama

query = input('Input: ')
sys_context = 'Keep your response to less than 10 words'

response = ollama.chat(
    model='llama3',
    messages=[
        {'role': 'system',
         'content': sys_context},
        {'role': 'user', 
        'content': query}
    ]
)

print('Output: ' + response['message']['content'])