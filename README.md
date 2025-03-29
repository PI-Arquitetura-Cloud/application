# CryptoNight - Projeto PI Arquitetura Cloud

Este é o repositório do projeto CryptoNight, desenvolvido para a disciplina de PI - Arquitetura Cloud.

# Link do Projeto
O projeto está hospedado no [Render](https://render.com/), uma plataforma de nuvem que simplifica a implantação de aplicações web, oferecendo suporte a diversas linguagens e frameworks.

Acesse o site do projeto: [CryptoNight](https://cryptocurrence-pi.onrender.com)

## Estrutura do Projeto

Este projeto está organizado em dois repositórios principais:

- `application`: Contém o código fonte do projeto
- `documentation`: Contém toda a documentação do projeto, incluindo:
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
