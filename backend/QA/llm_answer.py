import openai

CHATGPT_API_KEY = "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"
OPEN_AI_MODEL = "gpt-3.5-turbo"
openai.api_key = CHATGPT_API_KEY


def generate_chatgpt(prompt, open_ai_model=OPEN_AI_MODEL):
    response = openai.ChatCompletion.create(
        model=open_ai_model,
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )
    # generated_answer = response['choices'][0]['message']['content']
    messeage = ''
    for chunk in response:
        generated_answer = chunk['choices'][0]['delta']['content']
        print(generated_answer, end="")
        messeage += generated_answer
    return messeage


if __name__ == '__main__':
    generate_chatgpt('I am your brain. I produce your thoughts. I love you')