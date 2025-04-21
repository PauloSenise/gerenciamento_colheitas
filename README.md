# Gerenciamento de Colheitas

## Área do Agronegócio Tratada

Este projeto visa oferecer uma solução para a área de **gerenciamento de colheitas**, com foco na **otimização do processo e na redução de desperdícios**, seguindo os princípios e estratégias discutidos no material de referência.

## Contextualização e Justificativa

A complexidade e a importância econômica do agronegócio no Brasil demandam soluções eficientes para otimizar cada etapa da produção. Este projeto se concentra na fase crucial da colheita, buscando aplicar os conhecimentos de Python para desenvolver ferramentas que auxiliem no planejamento, acompanhamento e análise do processo.

A otimização da colheita, conforme as estratégias apresentadas, pode levar a uma significativa redução de perdas e ao aumento da produtividade. Ao apresentar um sistema que permite o registro, análise e acompanhamento dos dados da colheita, nosso objetivo é fornecer informações valiosas para tomadas de decisão mais assertivas.

## Funcionalidades (Baseado no Código Presente - `monitoramento_producao.py`)

Este script Python oferece um sistema interativo de gerenciamento de colheitas, permitindo aos usuários realizar as seguintes operações através de um menu no prompt de comando:

1.  **Registrar Nova Colheita:** Permite inserir dados de uma nova colheita, incluindo:
    * Data da colheita (no formato AAAA-MM-DD).
    * Área colhida em hectares (validação para garantir valor positivo).
    * Quantidade colhida em sacas de 60kg (validação para garantir valor positivo e inteiro).
    * Talhão/Parcela (campo de texto livre).
    * Tipo de Café (campo opcional de texto livre).
    * Safra (campo opcional de texto livre).
    Os dados inseridos são armazenados temporariamente em uma lista de dicionários na memória.

2.  **Listar Colheitas:** Exibe todos os registros de colheita atualmente armazenados na memória, mostrando detalhes como data, área, quantidade, talhão e, se informados, tipo de café e safra.

3.  **Calcular Produtividade Média:** Calcula e exibe a produtividade média da colheita, em sacas por hectare, com base nos registros existentes que possuem dados válidos de área e quantidade.

4.  **Filtrar Colheitas por Talhão:** Permite ao usuário inserir o nome de um talhão e exibe todos os registros de colheita correspondentes a esse talhão. A busca não diferencia maiúsculas e minúsculas.

5.  **Salvar Dados em Arquivo (JSON):** Salva todos os registros de colheita armazenados na memória em um arquivo chamado `colheitas.json`. Os dados são formatados em JSON para fácil leitura.

6.  **Carregar Dados em Arquivo (JSON):** Carrega os registros de colheita previamente salvos do arquivo `colheitas.json` para a memória. Se o arquivo não for encontrado ou estiver corrompido, inicia com uma lista de colheitas vazia.

7.  **Criar Tabela no Oracle:** Estabelece uma conexão com o banco de dados Oracle (utilizando as credenciais definidas no código) e cria uma tabela chamada `COLHEITAS` para armazenar os dados das colheitas, caso ela ainda não exista. A tabela inclui campos para data da colheita (chave primária junto com o talhão), área, quantidade, talhão (chave primária junto com a data), tipo de café e safra.

8.  **Salvar os Dados no Oracle:** Conecta-se ao banco de dados Oracle e insere os registros de colheita atualmente na memória na tabela `COLHEITAS`.

9.  **Carregar Banco de Dados do Oracle:** Conecta-se ao banco de dados Oracle e carrega todos os registros da tabela `COLHEITAS` para a memória. A data da colheita é formatada para o padrão AAAA-MM-DD.

10. **Deletar Colheita do Banco de Dados:** Permite ao usuário inserir a data e o talhão de uma colheita para deletar o registro correspondente do banco de dados Oracle. Também remove o registro da lista na memória.

11. **Salvar Dados em Arquivo (Texto):** Salva os registros de colheita em um arquivo de texto chamado `colheitas.txt`, utilizando o formato CSV (valores separados por vírgula), incluindo um cabeçalho com os nomes dos campos.

12. **Sair:** Encerra a execução do programa.

## Possíveis Futuras Funcionalidades (Inspiradas no Material)

* **Planejamento da Colheita:** Desenvolver funcionalidades para auxiliar no planejamento da colheita em diferentes épocas, considerando fatores como clima e previsão de safra.
* **Análise de Produtividade por Época:** Implementar relatórios e análises comparativas da produtividade em diferentes períodos do ano, identificando os melhores momentos para a colheita.

## Como Executar o Código

Para executar este script de gerenciamento de colheitas, siga as instruções abaixo:

1.  **Pré-requisitos:**
    * **Python:** Certifique-se de ter o Python instalado em seu sistema. Você pode verificar a instalação abrindo o terminal ou prompt de comando e digitando `python --version` ou `python3 --version`.
    * **Biblioteca `oracledb`:** Esta biblioteca é necessária para a funcionalidade de conexão com o banco de dados Oracle. Caso não a tenha instalada, você pode instalá-la utilizando o pip (gerenciador de pacotes do Python). Abra o terminal ou prompt de comando e execute:
        ```bash
        pip install oracledb
        ```
    * **Banco de Dados Oracle (Opcional):** Se você pretende utilizar as funcionalidades de salvar, carregar e deletar dados do Oracle (opções 7, 8, 9 e 10 do menu), você precisa ter o banco de dados Oracle instalado e configurado, além de ter as credenciais de acesso corretas (usuário, senha e DSN) no código (`conectar_oracle()` function). **Note:** As credenciais padrão no código são `user="system"`, `password="6364"` e `dsn="localhost:1521/xe"`. Você precisará ajustá-las conforme a sua configuração do Oracle.

2.  **Execução do Script:**
    * Salve o código Python em um arquivo chamado `monitoramento_producao.py` (ou outro nome de sua preferência).
    * Abra o terminal ou prompt de comando na pasta onde você salvou o arquivo.
    * O menu de opções será exibido no terminal, e você poderá interagir com o sistema digitando o número da opção desejada e seguindo as instruções.

3.  **Utilização:**
    * Siga as opções do menu para registrar novas colheitas, listar os registros, calcular a produtividade média, filtrar por talhão, salvar e carregar dados em arquivos JSON e de texto, interagir com o banco de dados Oracle e sair do programa.
    * As funcionalidades relacionadas ao Oracle (opções 7 a 10) só funcionarão corretamente se a conexão com o banco de dados for estabelecida com sucesso e a tabela `COLHEITAS` existir.


## Estruturas de Dados e Manipulação de Arquivos

Este projeto utiliza as seguintes estruturas de dados do Python e técnicas de manipulação de arquivos:

* **Listas:** A variável `registros_colheitas` é inicializada como uma lista vazia (`[]`). Esta lista é utilizada para armazenar os registros de cada colheita na memória durante a execução do programa. Cada elemento desta lista é um dicionário contendo os dados de uma colheita específica.

* **Tuplas:** Na função `registrar_colheita`, os dados da nova colheita são temporariamente armazenados em uma tupla chamada `novo_registro_tupla` antes de serem convertidos em um dicionário. A tupla serve como uma estrutura de dados imutável para organizar os dados coletados do usuário antes de serem formatados para o armazenamento principal.

* **Dicionários:** Cada registro de colheita é armazenado como um dicionário dentro da lista `registros_colheitas`. As chaves do dicionário representam os campos da colheita (por exemplo, 'data', 'area', 'quantidade', 'talhao', 'tipo', 'safra'), e os valores correspondem aos dados inseridos pelo usuário para cada campo. Essa estrutura facilita o acesso e a manipulação dos dados de cada registro.

* **Manipulação de Arquivos JSON:** O programa implementa funcionalidades para salvar e carregar os dados de colheita utilizando arquivos no formato JSON (`colheitas.json`).
    * **Salvar (Opção 5):** A função `salvar_dados()` utiliza a biblioteca `json` para escrever a lista de dicionários `registros_colheitas` em um arquivo JSON, com uma formatação indentada para melhor legibilidade.
    * **Carregar (Opção 6):** A função `carregar_dados()` utiliza a biblioteca `json` para ler os dados do arquivo `colheitas.json` e carregar os registros de volta para a lista `registros_colheitas` na memória. O tratamento de erros é implementado para casos em que o arquivo não é encontrado ou possui um formato JSON inválido.

* **Manipulação de Arquivos de Texto (CSV):** O programa também oferece a opção de salvar os dados em um arquivo de texto simples (`colheitas.txt`) no formato CSV (Comma Separated Values) através da função `salvar_dados_texto()` (Opção 11). Os dados de cada registro são escritos em uma linha, com os valores separados por vírgulas, e a primeira linha do arquivo contém o cabeçalho com os nomes dos campos.

## Conexão com Banco de Dados (Oracle)

Este projeto implementa a funcionalidade de interagir com um banco de dados Oracle para o armazenamento e recuperação persistente dos dados de colheita. As seguintes operações relacionadas ao Oracle estão disponíveis através do menu:

* **Conexão:** A função `conectar_oracle()` estabelece uma conexão com o banco de dados Oracle utilizando a biblioteca `oracledb`. As informações de conexão (usuário, senha e DSN) estão definidas diretamente na função. **É importante notar que as credenciais padrão no código são `user="system"`, `password="6364"` e `dsn="localhost:1521/xe"`, e podem precisar ser ajustadas para corresponder à sua configuração do Oracle.**

* **Criação de Tabela (Opção 7):** A função `criar_tabela_oracle()` verifica se a tabela `COLHEITAS` já existe no esquema do usuário conectado. Caso não exista, ela cria a tabela com a seguinte estrutura:
    * `data_colheita`: `DATE` (Não nulo, parte da chave primária)
    * `area`: `NUMBER` (Não nulo)
    * `quantidade`: `NUMBER` (Não nulo)
    * `talhao`: `VARCHAR2(50)` (Não nulo, parte da chave primária)
    * `tipo_cafe`: `VARCHAR2(50)` (Opcional)
    * `safra`: `VARCHAR2(20)` (Opcional)
    A chave primária é definida nas colunas `data_colheita` e `talhao`, garantindo a unicidade dos registros por data e local.

* **Salvar Dados no Oracle (Opção 8):** A função `salvar_oracle()` pega os registros de colheita atualmente armazenados na memória (na lista `registros_colheitas`) e os insere na tabela `COLHEITAS` do banco de dados Oracle. Os dados são inseridos utilizando prepared statements para evitar problemas de segurança e garantir a correta manipulação dos tipos de dados.

* **Carregar Dados do Oracle (Opção 9):** A função `carregar_oracle()` consulta todos os registros da tabela `COLHEITAS` no banco de dados Oracle e os carrega para a lista `registros_colheitas` na memória. A data da colheita, armazenada como um tipo `DATE` no Oracle, é formatada para uma string no formato `AAAA-MM-DD` ao ser carregada.

* **Deletar Colheita do Oracle (Opção 10):** A função `deletar_colheita_oracle()` permite ao usuário especificar a data e o talhão de um registro para ser removido da tabela `COL
