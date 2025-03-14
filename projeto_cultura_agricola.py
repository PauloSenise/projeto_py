# Criação dos vetores para 2 culturas agrícolas 
culturas = []
areas = []
insumos = []

# DEFINIÇÃO DAS FUNÇÕES

# Função para validar a opção digitada
def validar(entrada):
    valor = int(input(entrada))
    if valor == 0 or valor >6:
        print("""
        ----------------------
          OPÇÃO IVÁLIDA...!!
        ----------------------
       --------------------------
       Escolha uma Opção de 1 a 6
       --------------------------
              """)
    if valor <=6:
        return(valor)
    if valor >=1:
        return(valor)

# Esta função adiona a cultura e a área agrícola
def adicionar_cultura():
    cultura = input('\nDigite o nome da cultura agrícola...: ')
    tipo_area = input('Digite o formato da área (retangulo, circulo, triangulo): ')

    if tipo_area == "retangulo":
        comprimento = float(input("Digite o valor do comprimento: "))
        largura = float(input("Digite o valor da largura: "))
        area = comprimento * largura

    elif tipo_area == "circulo":
        raio = float(input("Digite o valor do raio: "))
        area = 2 * 3.141516 * raio * raio  
    
    elif tipo_area == "triangulo":
        base = float(input("Digite o valor da base: "))
        altura = float(input("Digite o valor da altura: "))
        area = (base * altura)/2
       
    # Adiciona items aos vetores
    culturas.append([f'- Cultura: {cultura}'])
    areas.append(area)

    #areas.append([f'{area:.2f} m²']) # ERRO: Está Armazenando na Lista o Conteúdo em formato de String
    print("""
         ---------------------------------
          Dados Gravados com Sucesso...!!
         ---------------------------------
          """)

# Função para cálculo do insumo
def adicionar_insumo():
    nome_cultura = input('Digite a cultura: ').strip().lower()  # Normaliza a entrada #.strip() retira " " 
                                                                # .lower() altera para letras minúsculas
    # Ajustando a busca para encontrar corretamente dentro das sublistas
    index = None
    for i, item in enumerate(culturas):
        if nome_cultura == item[0].replace('- Cultura: ', '').strip().lower():
            index = i
            break

    if index is None:
        print(f"""
              ----------------------------------------------
               Erro: A cultura '{nome_cultura}' não está cadastrada.
              ----------------------------------------------
              """)
        return  # Sai da função para evitar o erro
    # Insumos para o Café
    if nome_cultura == 'cafe':
        print("""\nTIPOS DE ADUBO PARA O PLANTIO DO CAFÉ CONFORME O SOLO:
1. Adubo Rico em Nitrogênio - Escolha: Torta de Mamona - 20 L/m
2. Adubo com Matéria Orgânica e Potássio - Escolha Casca de Café - 2 L/m
3. Adubo mais Equilibrado - Escolha Casca de Café - 10 L/m             
        """)
        adubo = int(input('Digite a opção de adubo: '))

        if adubo in [1, 2, 3]:  # Garante que a opção é válida
            quantidade = float(input("Quantidade por metro quadrado: "))
            total_insumo = quantidade * areas[index]  # Converte área para número
            insumos.append((nome_cultura, adubo, total_insumo))
            print(f"Para o plantio do {nome_cultura}, será necessário {total_insumo:.2f} litros de insumo do tipo {adubo}.")
        else:
            print("Opção de adubo inválida!")

    # Insumos para Laranja
    if nome_cultura == 'laranja':
        print("""\nTIPOS DE ADUBO PARA O PLANTIO DO CAFÉ CONFORME O SOLO:
1. Adubo Rico em Nitrogênio - Escolha: Torta de Mamona - 20 L/m
2. Adubo com Matéria Orgânica e Potássio - Escolha Casca de Café - 2 L/m
3. Adubo mais Equilibrado - Escolha Casca de Café - 10 L/m             
        """)
        adubo = int(input('Digite a opção de adubo: '))

        if adubo in [1, 2, 3]:  # Garante que a opção é válida
            quantidade = float(input("Quantidade por metro quadrado: "))
            total_insumo = quantidade * areas[index]  # Converte área para número
            insumos.append((nome_cultura, adubo, total_insumo))
            print(f"Para o plantio do {nome_cultura}, será necessário {total_insumo:.2f} litros de insumo do tipo {adubo}.")
        else:
            print("Opção de adubo inválida!")

# Função que lista todos os dados do vetor
def listar_dados():
    if culturas == []:
        print("""\n
              -------------------------
              Cadastro está vazio...!!!
              -------------------------
              """)
    if culturas != []:
        print("""
              ------------------
              Dados cadastrados:
              ------------------
              """)   
        for i in range(len(culturas)):  # Agora percorre os elementos dentro da sublista
            cultura = culturas[i][0]  # Obtém cada elemento corretamente
            area = f"{areas[i]:.2f} m²"  # Formata em número o valor da área ao exibir # Maneira correta 
            # area = areas[i][0]  # Obtém a área correspondente, ERRO: porém em formato de string que gerou problema na função atualizar_dados()
            print(f"{cultura} -> Área: {area}")

# Atualizar dados
def atualizar_dados():
        # Digitar o Nome
        nome = input('\nNome...:')
        # Verificar se existe o nome na lista
        for dado in culturas:
            if f'- Cultura: {nome}' in dado:
                for i in range(len(culturas)):
                    cultura = culturas[i][0]
                    for cultura in culturas:
                        index = culturas.index(cultura)
                        nova_area = float(input("Digite a nova área: "))
                        areas[index] = nova_area
                        print("Área atualizada com sucesso!")
                        break
            else:
                print('\nCultura agrícola não cadastrada...!!!')
     
# Função que apaga o registro de um contato
def deletar_dados():
    # Digitar o Nome
    nome = input('\nNome...:')
    # Verificar se existe o nome na lista
    for dado in culturas:
        if f'- Cultura: {nome}' in dado:
            print('\nContato encontrado...!!!')
            culturas.remove(dado)
            print('\nDADOS REMOVIDO COM SUCESSO!!')
            break
    else:
        print('\nDados não encontrado...!!!')
        
# PROGRAMA PRINCIPAL
# Função que exibe o menu de opções
def menu():
    print("""
      MENU DE OPÇÕES\n
1 - Adicionar Culturas
2 - Adicionar Insumo
3 - Listar Dados
4 - Atualizar Dados
5 - Deletar Dados
6 - Sair     
""")
    return  validar('Escolha uma opção: ')
       
while True:
    opcao = menu() # Loop infinito do menu
    if opcao == 1:
        adicionar_cultura()
    if opcao == 2:
        adicionar_insumo()
    if opcao == 3:
        listar_dados()
    if opcao == 4:
        atualizar_dados()
    if opcao == 5:
        deletar_dados()
    if opcao == 6:
        print('\nSaindo do programa...\n\n')
        break
    
    
