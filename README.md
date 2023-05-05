# Evasão - FastAPI

Este é um projeto que usa o framework FastAPI para construir uma API que permite realizar predições de evasão de alunos em cursos superiores.
Instalação

## Execução
Para executar a aplicação, siga as instruções abaixo:

    1. Clone este repositório em sua máquina local.
    2. Certifique-se de ter o Python 3.6 ou superior instalado.
    3. Crie um ambiente virtual para o projeto e ative-o.
    4. Instale as dependências usando o comando pip install -r requirements.txt.
    5. Execute o comando uvicorn app.main:app --reload para iniciar o servidor.

## Utilização

Com o servidor em execução, você pode acessar a documentação da API em http://localhost:8000/docs ou http://localhost:8000/redoc.

Existe um endpoint disponível:

    /predict: permite realizar uma predição de evasão de um aluno.

Você pode usar o endpoint /predict enviando uma solicitação POST contendo as informações do aluno em formato JSON. O servidor irá retornar uma resposta contendo a predição de evasão do aluno.

**Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar uma solicitação de pull para propor melhorias no projeto.**

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE.md) para detalhes.
