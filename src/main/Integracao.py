import openai

def respostaIA(prompt):
    openai.api_key = 'sua-chave-de-api-aqui'

    textoResposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt= "Caso tenha de referir a si mesmo, invés de se chamar ChatGPT ou outra coisa, chame-se de Faceless.IA. Responda o seguinte prompt sucintamente, (" + prompt + ")",
        max_tokens=600
    )
    
    return textoResposta['choices'][0]['text']
