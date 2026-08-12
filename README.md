# TODO API

API REST simples para gerenciamento de tarefas (CRUD completo), desenvolvida com Flask, Flask-SQLAlchemy e Marshmallow.

Este projeto foi criado como forma de aprender e praticar desenvolvimento backend com Python, aplicando conceitos de API REST, ORM, serialização de dados, validação de requisições e tratamento de erros.

## Tecnologias

- Python
- Flask
- Flask-SQLAlchemy
- Marshmallow
- SQLite

## Estrutura do projeto

```
todo-api/
├── app/
│ ├── __init__.py # cria e configura o app Flask (application factory)
│ ├── database.py # configuração da instância do SQLAlchemy
│ ├── models.py # define o modelo Task
│ ├── routes.py # define os endpoints da API
│ └── schemas.py # esquemas de validação e serialização (Marshmallow)
├── requirements.txt
├── run.py # ponto de entrada da aplicação
└── README.md
```

## Como rodar o projeto

1. Clone o repositório:
```bash
   git clone https://github.com/lucasbartolomeu1/project-todo.git
   cd project-todo/todo-api
```

2. Crie e ative o ambiente virtual:
```bash
   python -m venv venv
   source venv/bin/activate       # Linux/Mac (bash/zsh)
   source venv/bin/activate.fish  # Linux/Mac (fish)
```

3. Instale as dependências:
```bash
   pip install -r requirements.txt
```

4. Rode a aplicação:
```bash
   python run.py
```

O servidor sobe em `http://127.0.0.1:5000`. O banco SQLite (`instance/tasks.db`) é criado automaticamente na primeira execução.

## Endpoints

| Método | Rota            | Descrição                       |
|--------|-----------------|----------------------------------|
| GET    | `/tasks`        | Lista todas as tarefas           |
| GET    | `/tasks/<id>`   | Retorna uma tarefa específica    |
| POST   | `/tasks`        | Cria uma nova tarefa             |
| PUT    | `/tasks/<id>`   | Atualiza uma tarefa existente    |
| DELETE | `/tasks/<id>`   | Remove uma tarefa                |

## Exemplos de uso

Criar uma tarefa:
```bash
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Estudar Flask", "description": "Terminar o CRUD"}'
```

Listar tarefas:
```bash
curl http://127.0.0.1:5000/tasks
```

Atualizar uma tarefa:
```bash
curl -X PUT http://127.0.0.1:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done": true}'
```

Remover uma tarefa:
```bash
curl -X DELETE http://127.0.0.1:5000/tasks/1
```

Tentando criar uma tarefa sem título (erro de validação):
```bash
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"description": "Faltou o titulo"}'
```
Resposta (`400 Bad Request`):
```json
{
  "title": ["O titulo e obrigatorio."]
}
```

Buscando uma tarefa que não existe:
```bash
curl http://127.0.0.1:5000/tasks/999
```
Resposta (`404 Not Found`):
```json
{
  "message": "Recurso nao encontrado."
}
```

## Modelo de dados

```json
{
  "id": 1,
  "title": "Estudar Flask",
  "description": "Terminar o CRUD",
  "done": false
}
```

## Próximos passos

- Adicionar autenticação (JWT)
- Migrar de SQLite para PostgreSQL
- Adicionar testes automatizados (pytest)
- Adicionar paginação e filtros no `GET /tasks`