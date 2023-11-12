import openai

def respostaIA(prompt):
    openai.api_key = 'Chave api'

    textoResposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )

    return textoResposta['choices'][0]['text']
