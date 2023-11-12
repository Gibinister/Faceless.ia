import openai

def respostaIA(prompt):
    openai.api_key = 'Chave api'

    textoResposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt= "Responda o seguinte prompt sucintamente, caso ele toque em topicos controversos fale que não gostaria de responder este tipo de pergunta (" + prompt + ")",
        max_tokens=200
    )
    
    return textoResposta['choices'][0]['text']
