# Aluno: Paulo Henrique Senise - RM: 565781 - Turma:  1TIAOA - 2025/1.

import json
import oracledb

# Definição de lista vazia.
registros_colheitas = []

# OPÇÃO 1: Solicita os dados da colheita ao usuário, valida-os, armazena em tupla e adiciona ao registro como dicionário.
def registrar_colheita(registros):

    print("\n--- Registrar Nova Colheita (Usando Tupla Intermediária) ---")

    while True:
        data = input("Data da Colheita (AAAA-MM-DD): ")
        if not data:
            print("A data da colheita é obrigatória.")
            continue
        break

    while True:
        try:
            area = float(input("Área Colhida (em hectares): "))
            if area <= 0:
                print("A área deve ser um valor positivo.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número para a área.")

    while True:
        try:
            quantidade = int(input("Quantidade Colhida (em sacas de 60kg): "))
            if quantidade <= 0:
                print("A quantidade deve ser um valor positivo.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número inteiro para a quantidade.")

    talhao = input("Talhão/Parcela: ")
    tipo = input("Tipo de Café (opcional): ")
    safra = input("Safra (opcional): ")

    # Cria uma tupla com os dados da colheita.
    novo_registro_tupla = (data, area, quantidade, talhao, tipo, safra)

    # Converte a tupla em um dicionário
    novo_registro_dict = {
        'data': novo_registro_tupla[0],
        'area': novo_registro_tupla[1],
        'quantidade': novo_registro_tupla[2],
        'talhao': novo_registro_tupla[3],
        'tipo': novo_registro_tupla[4],
        'safra': novo_registro_tupla[5]
    }

    registros.append(novo_registro_dict)
    print("\nColheita registrada com sucesso!")

# OPÇÃO 2: Exibe todos os registros de colheita armazenados.
def listar_colheitas(registros):

    print("\n--- Listagem de Colheitas ---")
    if not registros:
        print("Nenhum registro de colheita encontrado.")
        return

    for i, registro in enumerate(registros):

        print(f"\nRegistro #{i+1}:")
        print(f"  Data: {registro['data']}")
        print(f"  Área: {registro['area']} hectares")
        print(f"  Quantidade: {registro['quantidade']} sacas")
        print(f"  Talhão: {registro['talhao']}")
        if registro.get('tipo'):
            print(f"  Tipo de Café: {registro['tipo']}")
        if registro.get('safra'):
            print(f"  Safra: {registro['safra']}")
    print("\n--- Fim da Listagem ---")

# OPÇÃO 3: Calcula e exibe a produtividade média da colheita. 
def calcular_produtividade_media(registros):
    
    print("\n--- Cálculo da Produtividade Média ---")
    if not registros:
        print("Nenhum registro de colheita encontrado para calcular a produtividade.")
        return

    soma_produtividade = 0
    total_registros = 0

    for registro in registros:
        area = registro.get('area')
        quantidade = registro.get('quantidade')

        if area and area > 0 and quantidade is not None:
            produtividade = quantidade / area
            soma_produtividade += produtividade
            total_registros += 1

    if total_registros > 0:
        media_produtividade = soma_produtividade / total_registros
        print(f"A produtividade média da colheita é de: {media_produtividade:.2f} sacas por hectare.")
    else:
        print("Não foi possível calcular a produtividade média devido à falta de dados válidos de área.")

# OPÇÃO 4: Filtra e exibe os registros de colheita por um talhão específico. 
def filtrar_colheitas_por_talhao(registros):

    print("\n--- Filtrar Colheitas por Talhão ---")
    if not registros:
        print("Nenhum registro de colheita encontrado para filtrar.")
        return

    talhao_busca = input("Digite o nome do talhão que deseja buscar: ")
    registros_encontrados = []

    for registro in registros:
        if registro.get('talhao', '').lower() == talhao_busca.lower():
            registros_encontrados.append(registro)

    if registros_encontrados:

        print(f"\nRegistros encontrados para o talhão '{talhao_busca}':")
        for i, registro in enumerate(registros_encontrados):
            print(f"\nRegistro #{i+1}:")
            print(f"  Data: {registro['data']}")
            print(f"  Área: {registro['area']} hectares")
            print(f"  Quantidade: {registro['quantidade']} sacas")
            print(f"  Talhão: {registro['talhao']}")
            if registro.get('tipo'):
                print(f"  Tipo de Café: {registro['tipo']}")
            if registro.get('safra'):
                print(f"  Safra: {registro['safra']}")
        print("\n--- Fim dos Registros Encontrados ---")
    else:
        print(f"\nNenhum registro de colheita encontrado para o talhão '{talhao_busca}'.")

# OPÇÂO 5: Salva os registros de colheita em um arquivo JSON.
def salvar_dados(registros, nome_arquivo="colheitas.json"):
    
    try:
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(registros, arquivo, indent=4)  # O 'indent=4' formata o JSON para melhor leitura
        print(f"\nDados salvos com sucesso no arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"\nErro ao salvar os dados no arquivo '{nome_arquivo}': {e}")

# OPÇÃO 6: Carrega os registros de colheita de um arquivo JSON.
def carregar_dados(nome_arquivo="colheitas.json"):
    
    try:
        with open(nome_arquivo, 'r') as arquivo:
            registros = json.load(arquivo)
        print(f"\nDados carregados com sucesso do arquivo '{nome_arquivo}'.")
        return registros
    except FileNotFoundError:
        print(f"\nArquivo '{nome_arquivo}' não encontrado. Iniciando com uma lista de colheitas vazia.")
        return []
    except json.JSONDecodeError:
        print(f"\nErro ao decodificar o arquivo '{nome_arquivo}'. O arquivo pode estar corrompido ou no formato errado. Iniciando com uma lista de colheitas vazia.")
        return []
    except Exception as e:
        print(f"\nErro ao carregar os dados do arquivo '{nome_arquivo}': {e}")
        return []
    
# OPÇÂO 7: Cria a tabela para armazenar os dados de colheita no Oracle, se não existir.
def conectar_oracle():
    
    try:
        # Substitua pelas suas informações de conexão
        conexao = oracledb.connect(
            user="system",
            password="6364",
            dsn="localhost:1521/xe"  
        )
        print("Conexão com o oracle estabelecida com sucesso!")
        return conexao
    except oracledb.Error as error:
        print(f"Erro ao conectar ao oracle (via oracledb): {error}")
        return None
    
def criar_tabela_oracle():
    
    conexao = conectar_oracle()
    cursor = None  # Inicializa cursor fora do try
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT table_name FROM user_tables WHERE table_name = 'COLHEITAS'")
            resultado = cursor.fetchone()
            if resultado:
                print("A tabela 'COLHEITAS' já existe.")
            else:
                comando_sql = """
                CREATE TABLE colheitas (
                    data_colheita DATE NOT NULL,
                    area NUMBER NOT NULL,
                    quantidade NUMBER NOT NULL,
                    talhao VARCHAR2(50) NOT NULL,
                    tipo_cafe VARCHAR2(50),
                    safra VARCHAR2(20),
                    CONSTRAINT colheitas_pk PRIMARY KEY (data_colheita, talhao)
                )
                """
                cursor.execute(comando_sql)
                conexao.commit()
                print("Tabela 'colheitas' criada com sucesso!")
        except oracledb.Error as error:
            print(f"Erro ao criar a tabela 'colheitas': {error}")
        finally:
            if cursor:
                cursor.close()
            conexao.close()

# OPÇÂO 8: Salva os registros de colheita no Oracle.
def salvar_oracle(registros):
    
    conexao = conectar_oracle()
    if conexao:
        try:
            cursor = conexao.cursor()
            comando_sql = """
            INSERT INTO colheitas (data_colheita, area, quantidade, talhao, tipo_cafe, safra)
            VALUES (TO_DATE(:data, 'YYYY-MM-DD'), :area, :quantidade, :talhao, :tipo, :safra)
            """
            for registro in registros:
                cursor.execute(comando_sql,
                               data=registro['data'],
                               area=registro['area'],
                               quantidade=registro['quantidade'],
                               talhao=registro['talhao'],
                               tipo=registro.get('tipo'),
                               safra=registro.get('safra'))
            conexao.commit()
            print(f"{len(registros)} registros salvos no oracle com sucesso!")
        except oracledb.Error as error:
            print(f"Erro ao salvar dados no oracle: {error}")
            conexao.rollback() # Em caso de erro, desfaz as alterações
        finally:
            if cursor:
                cursor.close()
            conexao.close()

#  OPÇÂO 9: Carrega os registros de colheita do Oracle.
def carregar_oracle():
    
    registros = []
    conexao = conectar_oracle()
    if conexao:
        try:
            cursor = conexao.cursor()
            comando_sql = "SELECT data_colheita, area, quantidade, talhao, tipo_cafe, safra FROM colheitas"
            cursor.execute(comando_sql)
            for row in cursor:
                registro = {
                    'data': row[0].strftime('%Y-%m-%d'), # Formata a data
                    'area': row[1],
                    'quantidade': row[2],
                    'talhao': row[3],
                    'tipo': row[4],
                    'safra': row[5]
                }
                registros.append(registro)
            print("Dados carregados do oracle com sucesso!")
        except oracledb.Error as error:
            print(f"Erro ao carregar dados do oracle: {error}")
        finally:
            if cursor:
                cursor.close()
            conexao.close()
    return registros

#  OPÇÂO 10: Deleta um registro de colheita do banco de dados Oracle.
def deletar_colheita_oracle(registros):
    
    conexao = conectar_oracle()
    cursor = None
    if conexao:
        try:
            cursor = conexao.cursor()
            print("\n--- Deletar colheita do banco de dados ---")
            data_deletar = input("Digite a data da colheita a ser deletada (AAAA-MM-DD): ")
            talhao_deletar = input("Digite o talhão da colheita a ser deletada: ")

            comando_sql = """
                DELETE FROM colheitas
                WHERE data_colheita = TO_DATE(:data, 'YYYY-MM-DD') AND talhao = :talhao
            """
            cursor.execute(comando_sql, data=data_deletar, talhao=talhao_deletar)
            registros_deletados = cursor.rowcount
            conexao.commit()

            if registros_deletados > 0:
                print(f"{registros_deletados} registro(s) deletado(s) do banco de dados.")
                # Opcional: Remover da lista na memória
                registros[:] = [reg for reg in registros if not (reg['data'] == data_deletar and reg['talhao'] == talhao_deletar)]
            else:
                print(f"Nenhum registro encontrado com a data '{data_deletar}' e talhão '{talhao_deletar}'.")

        except oracledb.Error as error:
            print(f"Erro ao deletar dados do Oracle: {error}")
            if conexao:
                conexao.rollback()
        finally:
            if cursor:
                cursor.close()
            conexao.close()

#  OPÇÂO 11: Salva os registros de colheita em um arquivo de texto (CSV).
def salvar_dados_texto(registros, nome_arquivo="colheitas.txt"):
    
    try:
        with open(nome_arquivo, 'w') as arquivo:
            # Escreve o cabeçalho (nomes dos campos)
            if registros:
                cabecalho = ",".join(registros[0].keys()) + "\n"
                arquivo.write(cabecalho)
                # Escreve os dados de cada registro
                for registro in registros:
                    linha = ",".join(str(registro.get(chave, '')) for chave in registros[0].keys()) + "\n"
                    arquivo.write(linha)
            print(f"\nDados salvos com sucesso no arquivo de texto '{nome_arquivo}'.")
    except Exception as e:
        print(f"\nErro ao salvar os dados no arquivo de texto '{nome_arquivo}': {e}")

######################################################################################
######################################################################################
# PROGRAMA PRINCIPAL
def exibir_menu():
    print("""
        MENU DE OPÇÕES\n
1 - Registrar Nova Colheita
2 - Listar Colheitas
3 - Calcular Produtividade Média
4 - Filtrar Colheitas por Talão
5 - Salvar Dados em Arquivo (JSON)
6 - Carregar Dados em Arquivo (JSON)
7 - Criar Tabela no Oracle
8 - Salvar os Dados no Oracle
9 - Carregar Banco de Dados do Oracle
10 - Deletar Colheita do Banco de Dados
11 - Salvar Dados em Arquivo (Texto)
12 - Sair
    """)

while True:
    exibir_menu()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        registrar_colheita(registros_colheitas)
    elif opcao == '2':
        listar_colheitas(registros_colheitas)
    elif opcao == '3':
        calcular_produtividade_media(registros_colheitas)
    elif opcao == '4':
        filtrar_colheitas_por_talhao(registros_colheitas)
    elif opcao == '5':
        salvar_dados(registros_colheitas)
    elif opcao == '6':
        registros_colheitas = carregar_dados()
    elif opcao == '7':
         criar_tabela_oracle()  # Garante que a tabela exista
    elif opcao == '8':
        salvar_oracle(registros_colheitas) # Opção para salvar os dados
    elif opcao == '9':
        registros_colheitas = carregar_oracle() # Opção para carregar os dados (era 8, agora é 9)
    elif opcao == '10':
        deletar_colheita_oracle(registros_colheitas) # Chama a função para deletar
    elif opcao == '11':
        salvar_dados_texto(registros_colheitas)
    elif opcao == '12':
        print('\nSaindo do programa...\n\n')
        break
    else:
        print('\nOpção inválida. Por favor, escolha uma opção do menu.\n')