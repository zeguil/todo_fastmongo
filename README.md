# Todo FastMongo Async
Este é um projeto simples desenvolvido com FastAPI e MongoDB para gerenciar tarefas (TODOs). O projeto inclui testes unitários usando pytest para garantir a funcionalidade correta da API e a integridade dos dados no banco de dados MongoDB.

## Funcionalidades

- **Criar uma nova tarefa**: Adiciona uma nova tarefa com título, descrição e estado de conclusão.
- **Listar tarefas**: Retorna todas as tarefas cadastradas.
- **Marcar tarefa como concluída**: Atualiza o estado de conclusão de uma tarefa existente.
- **Remover uma tarefa**: Exclui uma tarefa do sistema.

## Como Baixar e Executar

### Pré-requisitos

Certifique-se de ter o Python 3.12+ e o Poetry instalados.

### Instalação

```bash
git clone https://github.com/seu-usuario/todo-fastmongo.git
cd todo-fastmongo
poetry install
```

### Configuração do MongoDB

Certifique-se de ter um servidor MongoDB em execução. Você pode configurar a conexão com o MongoDB editando o arquivo todo_fastmongo/database.py se necessário.

caso tenha o docker instalado em sua máquina, pode usar o comando:
```
   docker run -d -p 27017:27017 --name mongodb mongo
```

### Executando a Aplicação
```
task run
```
A aplicação estará disponível em http://localhost:8000.

### Executando os Testes
```
poetry test
```

### Desenvolvimento Baseado em Testes (TDD)
Este projeto segue o princípio do Test-Driven Development (TDD), uma abordagem de desenvolvimento de software onde:

#### 1. Escrever um Teste: Primeiro, escrevemos um teste automatizado que define uma funcionalidade ou melhoria desejada.
#### 2. Executar o Teste: Em seguida, executamos o teste para verificar se ele falha, garantindo que ele realmente testa algo.
#### 3. Escrever o Código: Escrevemos o código necessário para passar no teste.
#### 4. Executar Todos os Testes: Todos os testes automatizados são executados para garantir que o novo código não quebrou nada existente.
#### 5. Refatorar: Refatoramos o código para melhorar sua estrutura ou desempenho, mantendo todos os testes passando.


### Estrutura do Código
```
todo_fastmongo/
├── app.py           # Configuração do FastAPI
├── database.py      # Configuração e operações com MongoDB
├── models.py        # Definição dos modelos de dados
├── routes.py        # Definição das rotas da API
tests/
├── conftest.py      # Configuração global de testes
├── test_db.py       # Testes relacionados ao banco de dados
├── test_routers.py  # Testes das rotas da API
poetry.lock          # Arquivo lock das dependências do Poetry
pyproject.toml       # Arquivo de configuração do Poetry
README.md            # Este arquivo


```