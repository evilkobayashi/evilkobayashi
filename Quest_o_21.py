texto_original = "a sorte esta lancada e o rubicao foi cruzado"
mensagem_cifrada = "n hzcal lhao yhujhkh l v cyfpjhv mvp jybchkv"

# ---------------------------------------------------------
# (a) Cifrar
# Desloca cada letra minúscula 'chave' posições.
# Utiliza a tabela ASCII: 'a' é 97.
# ---------------------------------------------------------
def cifrar(texto, chave):
    resultado = ""
    for char in texto:
        # Verifica se o caractere é uma letra minúscula
        if 'a' <= char <= 'z':
            # Converte a letra para uma posição de 0 a 25
            posicao_alfabeto = ord(char) - ord('a')
            # Aplica o deslocamento com a "volta" usando o módulo (%) 26
            nova_posicao = (posicao_alfabeto + chave) % 26
            # Converte de volta para o caractere ASCII
            resultado += chr(nova_posicao + ord('a'))
        else:
            # Se for espaço ou pontuação, não altera
            resultado += char
    return resultado

print("--- (a) Cifrar ---")
teste_cifra = cifrar(texto_original, 13)
print(f"Texto cifrado com chave 13: '{teste_cifra}'")


# ---------------------------------------------------------
# (b) Decifrar
# Reutiliza a função cifrar, mas com a chave inversa (26 - k)
# ---------------------------------------------------------
def decifrar(texto, chave):
    return cifrar(texto, 26 - chave)

print("\n--- (b) Decifrar ---")
teste_decifra = decifrar(teste_cifra, 13)
print(f"Texto decifrado: '{teste_decifra}'")
print(f"Recuperou o original? {teste_decifra == texto_original}")


# ---------------------------------------------------------
# (c) Análise de frequência
# Restrição: usar dicionário com laço e .get() (SEM collections.Counter)
# ---------------------------------------------------------
def frequencia(texto):
    freq = {}
    for char in texto:
        if char != ' ': # Ignorando espaços conforme o enunciado
            # Pega o valor atual (ou 0 se não existir) e soma 1
            freq[char] = freq.get(char, 0) + 1
    return freq

print("\n--- (c) Análise de frequência ---")
freq_cifrada = frequencia(mensagem_cifrada)
# Ordenando de forma decrescente pelo valor (item[1])
letras_frequentes = sorted(freq_cifrada.items(), key=lambda item: item[1], reverse=True)

print("As 5 letras mais frequentes na mensagem cifrada:")
for letra, contagem in letras_frequentes[:5]:
    print(f"Letra '{letra}': {contagem} vezes")


# ---------------------------------------------------------
# (d) Quebrar a cifra
# A letra mais frequente corresponde ao "a" original.
# ---------------------------------------------------------
print("\n--- (d) Quebrar a cifra ---")
# Pega a letra no topo do ranking (índice 0 da lista ordenada)
letra_mais_frequente_cifrada = letras_frequentes[0][0]

# Calcula a distância entre a letra mais frequente e a letra 'a'
chave_provavel = (ord(letra_mais_frequente_cifrada) - ord('a')) % 26

texto_quebrado = decifrar(mensagem_cifrada, chave_provavel)

print(f"Letra mais frequente encontrada: '{letra_mais_frequente_cifrada}'")
print(f"Chave provável calculada: {chave_provavel}")
print(f"Texto decifrado: '{texto_quebrado}'")


# ---------------------------------------------------------
# (e) Histograma horizontal
# Restrição: usar sorted(key=) com reverse=True
# ---------------------------------------------------------
print("\n--- (e) Histograma horizontal ---")
freq_original = frequencia(texto_original)
# Ordena a frequência do texto original
freq_original_ordenada = sorted(freq_original.items(), key=lambda item: item[1], reverse=True)

for letra, contagem in freq_original_ordenada:
    # Multiplica o caractere '#' pela quantidade de vezes que a letra apareceu
    barras = '#' * contagem
    print(f"{letra} | {barras} {contagem}")