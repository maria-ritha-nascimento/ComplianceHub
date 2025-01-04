# ComplianceHub

Bem-vindo ao **ComplianceHub**, uma plataforma para gestão de riscos e conformidade. Este projeto foi desenvolvido com o objetivo de fornecer ferramentas para identificar, gerenciar e mitigar riscos corporativos, além de garantir conformidade regulatória.

---

## 📋 Descrição do Projeto

O **ComplianceHub** é uma aplicação backend desenvolvida em Python, utilizando **FastAPI**, que oferece:

- Cadastro e consulta de riscos.
- API bem documentada com **Swagger** para facilitar a integração.
- Persistência de dados utilizando **SQLAlchemy** e suporte a diferentes bancos de dados.
- Estrutura escalável e modular, projetada para facilitar manutenção e expansão.

---

## ⚙️ Descrição Técnica

### **Tecnologias Utilizadas**
- **Linguagem:** Python 3.10+
- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Banco de Dados:** SQLite (padrão, mas expansível para PostgreSQL, MySQL, etc.)
- **Autenticação:** JWT (JSON Web Tokens) [em desenvolvimento]
- **Documentação:** Swagger/OpenAPI (disponível em `/docs`)
- **Testes Automatizados:** Pytest

### **Estrutura do Projeto**
```plaintext
ComplianceHub/
├── app/
│   ├── __init__.py
│   ├── main.py          # Ponto de entrada da aplicação
│   ├── models/          # Definição de modelos de dados (ORM)
│   ├── routes/          # Rotas da API
│   ├── schemas/         # Validação e serialização de dados (Pydantic)
│   ├── services/        # Regras de negócio e lógica de aplicação
│   ├── config.py        # Configurações e conexão com o banco de dados
├── tests/               # Testes automatizados com Pytest
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação do projeto
├── run.py               # Script para iniciar o servidor
```

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e executar o **ComplianceHub** em sua máquina local.

### **1. Pré-requisitos**
- Python 3.10 ou superior instalado.
- Git instalado para clonar o repositório.

### **2. Clonar o Repositório**
```bash
git clone https://github.com/maria-ritha-nascimento/ComplianceHub.git
cd ComplianceHub
```

### **3. Configurar o Ambiente Virtual**
Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### **4. Instalar Dependências**
Instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### **5. Configurar o Banco de Dados**
O banco de dados padrão é o **SQLite**. Para utilizá-lo, nenhuma configuração adicional é necessária. Se desejar usar outro banco, edite a variável `DATABASE_URL` no arquivo `app/config.py`.

### **6. Iniciar o Servidor**
Execute o servidor com o comando:
```bash
python run.py
```

O servidor estará disponível em `http://127.0.0.1:8000`. A documentação interativa estará acessível em `http://127.0.0.1:8000/docs`.

---

## 🛠️ Executar os Testes

Para garantir que o projeto está funcionando corretamente, execute os testes automatizados:
```bash
pytest
```

---

## 📚 Documentação da API

A documentação da API está disponível no formato **Swagger** em `/docs`:
- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **OpenAPI JSON:** `http://127.0.0.1:8000/openapi.json`

---

## 🌟 Contribuições

Contribuições são bem-vindas! Para colaborar:

1. Faça um fork do projeto.
2. Crie uma branch para suas alterações:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça o commit das alterações:
   ```bash
   git commit -m "Minha nova feature"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request no repositório original.

---

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas, entre em contato através do [repositório no GitHub](https://github.com/maria-ritha-nascimento/ComplianceHub.git).
