import openai

def respostaIA(prompt):
    openai.api_key = 'Chave api'

    textoResposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt= "Caso tenha de referir a si mesmo, invés de se chamar ChatGPT ou outra coisa, chame-se de Faceless.IA. Responda o seguinte prompt sucintamente, (" + prompt + ")",
        max_tokens=200
    )
    
    return textoResposta['choices'][0]['text']
