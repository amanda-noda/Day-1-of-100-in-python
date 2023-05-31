import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

## Gera uma senha de acordo com o tamanho que vc digitar, caso queira uma senha de 8 digitos, o gerador gera uma senha de 8 digitos e assim por diante.
tamanho_senha = int(input("Digite o tamanho desejado para a senha: "))
senha_gerada = gerar_senha(tamanho_senha)
print("Senha gerada:", senha_gerada)
