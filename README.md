# 📚 API de Livros — Flask

API REST simples para gerenciar uma lista de livros, construída com **Flask**. Permite consultar, criar, editar e excluir livros através de operações CRUD básicas.

## 🛠️ Tecnologias

- Python
- Flask

## ▶️ Como rodar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o arquivo:
```bash
python app.py
```

3. A API vai rodar em:
```
http://localhost:5000
```

## 📌 Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/livros` | Retorna todos os livros |
| `GET` | `/livros/<id>` | Retorna um livro pelo ID |
| `POST` | `/livros` | Adiciona um novo livro |
| `PUT` | `/livros/<id>` | Atualiza um livro existente |
| `DELETE` | `/livros/<id>` | Remove um livro pelo ID |

### Exemplo de livro (JSON)

```json
{
  "id": 4,
  "titulo": "1984",
  "autor": "George Orwell"
}
```

### Exemplos de uso

**Listar todos os livros**
```
GET /livros
```

**Buscar um livro por ID**
```
GET /livros/1
```

**Criar um novo livro**
```
POST /livros
Content-Type: application/json

{
  "id": 4,
  "titulo": "1984",
  "autor": "George Orwell"
}
```

**Editar um livro**
```
PUT /livros/1
Content-Type: application/json

{
  "titulo": "O Senhor dos Anéis - As Duas Torres"
}
```

**Excluir um livro**
```
DELETE /livros/1
```

## ⚠️ Observações

- Os dados são armazenados apenas em memória (lista `livros`) — ao reiniciar a aplicação, tudo volta ao estado inicial.
- Na rota `POST /livros`, `request.get_json` está sendo usado sem os parênteses (`()`), então na prática ele adiciona a *referência da função*, não o JSON enviado. Para funcionar como esperado, o correto é `request.get_json()`.
- As rotas `GET /livros/<id>`, `PUT /livros/<id>` e `DELETE /livros/<id>` não retornam um erro tratado (ex: `404`) quando o ID não existe — nesse caso a API retorna `None`/lista vazia sem avisar que o livro não foi encontrado.

## 📝 Possíveis melhorias

- [ ] Corrigir `request.get_json()` na criação de livro
- [ ] Adicionar tratamento de erro `404` quando o ID não for encontrado
- [ ] Validar os dados recebidos (ex: campos obrigatórios `titulo` e `autor`)
- [ ] Persistir os dados em um banco de dados em vez de lista em memória
