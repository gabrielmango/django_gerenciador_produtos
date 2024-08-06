# Gerenciador de Produtos

Este é um projeto Django para gerenciar produtos em uma aplicação web. Inclui funcionalidades para criar, editar, e visualizar produtos, bem como um formulário de contato para enviar mensagens por e-mail.

## Requisitos

- Python 3.x
- Django
- Django StdImageField (para manipulação de imagens)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/gabrielmango/django_gerenciador_produtos.git
   cd gerenciador-de-produtos
   ```

2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados:**

   Atualize as configurações do banco de dados no arquivo `settings.py` conforme necessário.

5. **Execute as migrações:**

   ```bash
   python manage.py migrate
   ```

6. **Inicie o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

   A aplicação estará disponível em `http://127.0.0.1:8000/`.

## Modelos

### Produto

- **nome**: Nome do produto.
- **preco**: Preço do produto.
- **estoque**: Quantidade disponível no estoque.
- **imagem**: Imagem do produto (com variação thumbnail).
- **slug**: Slug gerado automaticamente a partir do nome.

## Formulários

### ContatoForm

Um formulário para envio de mensagens de contato por e-mail, incluindo os campos: `nome`, `email`, `assunto`, e `mensagem`.

### ProdutoModelForm

Um formulário de modelo para criar e editar produtos, incluindo os campos: `nome`, `preco`, `estoque`, e `imagem`.

## Funcionalidades

- **Gerenciamento de Produtos**: Criação, edição e listagem de produtos com imagens.
- **Formulário de Contato**: Envio de mensagens por e-mail.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
