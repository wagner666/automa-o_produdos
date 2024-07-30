import pyautogui as pg
from time import sleep

# CMD-python -m mouseinfo

# 1 - Clicar e digitar meu usuário
pg.click(729,384, duration=0.5)
pg.write('wagner')
sleep(1)  # Adicione um delay
# 2- Clicar e digitar minha senha
pg.click(728,410, duration=0.5)
pg.write('123')
sleep(1)  # Adicione um delay
# 3 - Clicar em "Entrar"
pg.click(598,438, duration=0.5)
sleep(2)  # Adicione um delay maior para a página carregarProduto
# 4 - Extrair cada produto
with open('produtos.txt', 'r') as arquivo: # 'with open'=para abrir arquivo no python 'r'= para leitura ','= para saber das virgulas
    for linha in arquivo: # para cada linha do arquivo
        produto = linha.split(',')[0] # separa por virgula. [0]= acessar a primeira linha
        quantidade = linha.split(',')[1] # [1]=a segunda linha [2]=a terceira linha
        preco = linha.split(',')[2] # [2]=a terceira linha
        # 1 - clicar e digitar produto
        # Debugging
        #print(f"Produto: {produto}, Quantidade: {quantidade}, Preço: {preco}")
        pg.click(451,369,duration=0.5)
        pg.write(produto)
        sleep(1)  # Adicione um delay
        # 2 - clicar e digitar quantidade
        pg.click(441,396,duration=0.5)
        pg.write(quantidade)
        sleep(1)  # Adicione um delay
        # 3 - clicar e digitar preço
        pg.click(429,424,duration=0.5)
        pg.write(preco)
        sleep(1)  # Adicione um delay
        #  4 - clicar em registrar
        pg.click(320,584,duration=0.5)
        sleep(1)
