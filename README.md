
# API de Autenticação e Cadastro de Usuários

Este projeto fornece uma API simples para autenticação e cadastro de usuários. A API possui dois endpoints principais:

- **/usuarios/login**: Realiza o login de um usuário.
- **/usuarios/cadastro**: Realiza o cadastro de um novo usuário.

## Endpoints

### 1. **POST /usuarios/login**
Este endpoint permite o login de um usuário.

#### Request
O corpo da requisição deve conter os seguintes dados:

```json
{
    "email": "rw@exemplo.com",
    "senha": "senha123"
}
```

- **email**: O e-mail do usuário.
- **senha**: A senha do usuário.

#### Response
Em caso de sucesso, a resposta será:

```json
{
    "idUsuario": 3,
    "mensagem": "Bem-vindo"
}
```

Onde:
- **idUsuario**: O identificador único do usuário.
- **mensagem**: Uma mensagem de boas-vindas.

### 2. **POST /usuarios/cadastro**
Este endpoint permite o cadastro de um novo usuário.

#### Request
O corpo da requisição deve conter os seguintes dados:

```json
{
    "nome": "Robin",
    "sobrenome": "Wood",
    "email": "rw@exemplo.com",
    "senha": "senha123"
}
```

- **nome**: O primeiro nome do usuário.
- **sobrenome**: O sobrenome do usuário.
- **email**: O e-mail do usuário.
- **senha**: A senha do usuário.

#### Response
Em caso de sucesso, a resposta será:

```json
{
    "idUsuario": 3,
    "mensagem": "Usuário cadastrado com sucesso!"
}
```

Onde:
- **idUsuario**: O identificador único do usuário.
- **mensagem**: Uma mensagem confirmando o cadastro.

## Como Usar

1. Faça uma requisição POST para o endpoint `/usuarios/login` ou `/usuarios/cadastro`.
2. Forneça os dados apropriados no corpo da requisição.
3. A resposta conterá a mensagem apropriada e o `idUsuario` correspondente.

## Dependências

- Django (ou outro framework backend conforme necessário)
- Python 3.x
- Outros requisitos específicos do seu ambiente.

## License

Este projeto está licenciado sob a MIT License - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
