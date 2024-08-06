# Sistema de Busca por Similaridade Semântica

Este projeto é uma aplicação que utiliza processamento de linguagem natural (PLN) e um banco de dados vetorial para realizar buscas por similaridade semântica em um conjunto de dados. O sistema foi desenvolvido utilizando a biblioteca Sentence Transformers para geração de embeddings e o Milvus para armazenamento e busca vetorial.

## Índice

- [Objetivo](#objetivo)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Contribuição](#contribuição)

## Objetivo

O objetivo deste projeto é demonstrar como integrar modelos de embeddings de texto com um banco de dados vetorial para realizar buscas por similaridade semântica. O sistema permite a inserção de dados, a geração de embeddings e a execução de consultas semânticas para encontrar registros semelhantes.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- Python 3.8 ou superior
- Docker (para uso do Milvus)
- pip (para instalação das dependências)

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/PedroHIS/PLN_2024_Soares_Pedro.git
cd PLN_2024_Soares_Pedro
```
### 2. Instalar dependências

Crie um ambiente virtual e instale as dependências listadas em requirements.txt:

```bash
python -m venv venv
source venv/bin/activate  # Para Windows use: venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Configurar Docker

Certifique-se de que o Docker está instalado e em execução. O projeto inclui um arquivo docker-compose.yml para configurar o Milvus.
```bash
docker-compose up -d
```
## Configuração

### Arquivo requirements.txt

Certifique-se de que o arquivo requirements.txt contém as seguintes dependências:

```bash
pandas
sentence-transformers
pymilvus
```

### Arquivo docker-compose.yml

O arquivo docker-compose.yml configura o Milvus. Certifique-se de que está configurado conforme suas necessidades.

## Uso

### 1. Preparar os dados

Modifique o caminho no arquivo src/main.py para apontar para o arquivo JSON com o conjunto de dados que você deseja usar.

### 2. Executar o script principal

```bash
python src/main.py
```
O script realiza as seguintes etapas:

  1. Carrega e prepara os dados.
  2. Gera embeddings para o texto usando o modelo de Sentence Transformers.
  3. Conecta-se ao Milvus e cria uma coleção.
  4. Insere dados na coleção e cria índices.
  5. Realiza buscas por similaridade semântica com consultas padrão ou personalizadas.

### 3. Testar buscas

O script inclui consultas de teste, mas você pode modificar as consultas diretamente no código para testar diferentes cenários.

## Contribuição

Se você deseja contribuir para este projeto, siga as etapas abaixo:

  1. Faça um fork do repositório.
  2. Crie uma nova branch para suas alterações.
  3. Realize suas alterações e adicione testes conforme necessário.
  4. Envie um pull request com uma descrição clara das mudanças.