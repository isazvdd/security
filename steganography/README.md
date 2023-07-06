# Esteganografia

Esta pasta contém dois scripts que permitem a inserção de um texto em uma imagem, juntamente com alguns arquivos de exemplo para essa prática.

## Executando localmente

Para executar esses scripts em sua máquina você precisa ter o
[Python 3](https://www.python.org/) instalado.

### Instalação

1. Clone o repositório

    ```
    git clone https://github.com/isazvdd/security
    ```
2. Abra a pasta [`steganography`](../steganography/) no terminal
   ```
    cd security/steganography
    ```
3. Crie um ambiente virtual python
    ```
    python3 -m venv .venv
    ```
4. Ative o ambiente virtual
    ```
    source .venv/bin/activate
    ```
5. Instale as dependências
    ```
    pip install -r requirements.txt
    ```
### Escondendo a mensagem em uma imagem PNG
O exemplo a seguir utiliza a imagem e o arquivo de texto fornecidos nos exemplos. Para realizar o procedimento com outros arquivos, basta substituir os caminhos dos arquivos desejados nos comandos.
1. Execute o script `hide.py` passando o caminho da imagem e o caminho do
arquivo de texto com a mensagem secreta:
    ```
    python3 ./hide.py labepi.png secret.txt
    ```
### Recuperando a mensagem a partir da imagem
O exemplo a seguir utiliza a imagem com a mensagem secreta fornecida nos exemplos. Para realizar o procedimento com outros arquivos, basta substituir os caminhos dos arquivos desejados nos comandos. Opcionalmente, você pode fornecer um nome de arquivo de saída.
1. Execute o script `show.py` passando o caminho da imagem com a mensagem secreta, opcionalmente você pode passar um argumento para o nome do arquivo de saída:
    ```
    python3 ./show.py secret.png nome-do-arquivo.txt
    ```