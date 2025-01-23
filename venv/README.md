Descrição do Projeto:

Nome: TaskManagerApp
Objetivo: Um aplicativo que permite aos usuários criar, gerenciar e acompanhar tarefas, com recursos como categorias, prazos e filtros.
Funcionalidades Planejadas:

    Cadastro de Usuários:
        Registro e login.
        Hash de senhas com a biblioteca bcrypt.

    Gestão de Tarefas:
        Criação, edição e exclusão de tarefas.
        Organização por categorias e prioridades.
        Marcar tarefas como concluídas.

    Banco de Dados:
        Integração com SQLite para armazenamento.
        Relacionamentos: Usuários x Tarefas.

    Interface Gráfica:
        Desenvolvida com Tkinter ou PyQt.
        Lista de tarefas com filtros (por status, categoria, ou prazo).

    Histórico de Tarefas:
        Visualizar tarefas concluídas e excluídas.

    Funcionalidades Extras:
        Exportar lista de tarefas para arquivo (CSV ou PDF).
        Notificações de prazos (opcional).

Tecnologias e Ferramentas:

    Linguagem: Python 3.x
    Interface Gráfica: Tkinter ou PyQt5
    Banco de Dados: SQLite
    Versionamento: Git e GitHub
    Outras Bibliotecas:
        sqlite3 (para banco de dados).
        bcrypt (para segurança de senhas).
        pandas (para exportação de dados).


---------------TASK------------------ 

TaskManagerApp/
├── app/
│   ├── __init__.py
│   ├── database.py       # Conexão e operações com o banco de dados
│   ├── models.py          # Definições de tabelas e classes
│   ├── views.py           # Interface gráfica
│   ├── controllers.py    # Lógica de negócio
│   └── utils.py           # Funções auxiliares (ex.: validações, hash)
├── tests/
│   ├── test_database.py  # Testes de integração com o banco
│   ├── test_views.py     # Testes para a interface gráfica
│   └── test_models.py    # Testes unitários para as classes
├── assets/
│   ├── icons/            # Icones ou imagens usadas na interface
│   └── styles.css        # Estilo customizado para Tkinter ou PyQt
├── .gitignore            # Arquivos a serem ignorados pelo Git
├── README.md             # Descrição do projeto
├── requirements.txt      # Dependências do projeto
└── main.py               # Ponto de entrada do aplicativo