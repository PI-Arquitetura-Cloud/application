# CryptoNight - Projeto PI Arquitetura Cloud

Este é o repositório do projeto CryptoNight, desenvolvido para a disciplina de PI - Arquitetura Cloud.

## Estrutura do Projeto

Este repositório está organizado em duas branches principais:

- `main`: Contém o código fonte do projeto
- `docs`: Contém toda a documentação do projeto, incluindo:
  - Cronograma
  - MVP
  - Documentação técnica
  - Arquitetura
  - Outros documentos relacionados

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/CryptoNight.git
cd CryptoNight
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executando o Projeto

#### Modo Desenvolvimento
```bash
python app.py
```

#### Modo Produção (com Gunicorn)
```bash
gunicorn -c gunicorn_config.py app:app
```

O aplicativo estará disponível em `http://localhost:8000`

## 📚 Documentação

Para acessar a documentação completa do projeto, incluindo cronograma, MVP e outros documentos, acesse a branch `docs`:

```bash
git checkout docs
```

Ou acesse diretamente através do GitHub na branch `docs`.

## 🛠️ Tecnologias Utilizadas

- Flask
- Gunicorn
- BeautifulSoup4
- Requests
- Bootstrap (para interface web)

## 📝 Estrutura de Arquivos

```
CryptoNight/
├── app.py              # Aplicação principal
├── gunicorn_config.py  # Configuração do Gunicorn
├── requirements.txt    # Dependências do projeto
├── templates/         # Templates HTML
│   └── index.html
└── db/               # Diretório para armazenamento de dados
```

## 👥 Autores

Erick dos Santos Cirico 
Vinícius Raimundo la Serra
