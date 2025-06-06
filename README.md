
# API - Projeto Django

Este é um projeto de API construído com Django e Django REST Framework, configurado para funcionar com Docker.

## 🚀 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## 📁 Estrutura do Projeto

```
api-main/
├── api/                    # Aplicação principal Django
│   ├── models/             # Modelos de dados
│   ├── viewset/            # ViewSets personalizados
│   ├── urls.py             # URLs da aplicação
│   └── settings.py         # Configurações do Django
├── manage.py               # Script de gerenciamento Django
├── docker-compose.yml      # Configuração do Docker Compose
└── .gitignore              # Arquivos ignorados pelo Git
```

## ⚙️ Como Rodar

### Com Docker

1. **Suba os containers**:
   ```bash
   docker-compose up --build
   ```

2. **Acesse a aplicação**:
   Normalmente estará disponível em `http://localhost:8000`

### Sem Docker

1. Crie um ambiente virtual e ative:
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

4. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

## 🧪 Testes

Você pode rodar os testes com:

```bash
python manage.py test
```

## 📌 Contribuições

Contribuições Kevin.

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).
