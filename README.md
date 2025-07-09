
# App Bills Reminder

Aplicativo simples para controle e lembrete de contas a pagar, desenvolvido em Django.

---

## Descrição

O **App Bills Reminder** é um sistema web que permite ao usuário cadastrar suas contas, visualizar as próximas a vencer e controlar quais já foram pagas. Ideal para quem deseja organizar suas finanças pessoais e nunca mais esquecer de uma data de vencimento.

---

## Funcionalidades

- Cadastro de contas com título, valor, data de vencimento e status de pagamento.
- Listagem de contas com filtros para contas pagas e não pagas.
- Visualização das contas ordenadas por data de vencimento.
- Administração via painel do Django para gerenciar contas facilmente.

---

## Tecnologias utilizadas

- Python 3.x
- Django 4.x
- SQLite (banco de dados padrão, pode ser alterado)
- HTML/CSS (templates padrão do Django)

---

## Como usar

### Pré-requisitos

- Python 3 instalado
- pip instalado

### Passos para rodar o projeto localmente

1. Clone este repositório:
   ```bash
   git clone https://github.com/LinuxEater/app-bills-reminder.git
   ```

2. Entre na pasta do projeto:
   ```bash
   cd app-bills-reminder
   ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate     # Windows
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Faça as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

6. Crie um superusuário para acessar o admin:
   ```bash
   python manage.py createsuperuser
   ```

7. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

8. Acesse o sistema em:
   ```
   http://127.0.0.1:8000/
   ```

9. Para acessar o painel admin, vá para:
   ```
   http://127.0.0.1:8000/admin/
   ```

---

## Contribuição

Contribuições são bem-vindas!  
Para contribuir, faça um fork do projeto, crie uma branch com a sua feature ou correção e envie um pull request.

---

## Contato

Moisés Souza Santos  
Email: moisessouzasantos001@gmail.com  
GitHub: [https://github.com/LinuxEater](https://github.com/LinuxEater)

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

Made with ❤️ by Moisés Souza Santos
