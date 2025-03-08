Biblioteca Virtual - Projeto em Django
Este projeto é uma biblioteca virtual desenvolvida em Django, utilizando HTML e CSS para a interface. O sistema permite o gerenciamento de livros, empréstimos e devoluções, além de oferecer uma experiência personalizada para usuários registrados.

Funcionalidades Principais
Autenticação e Perfil do Usuário
Login e Registro: Autenticação de usuários com validações.

Perfil Personalizado: Exibe o nome do usuário logado na tela inicial.

Gerenciamento de Livros
Listagem de Livros: Tabela com informações dos livros (nome, gênero, quantidade de páginas e quantidade disponível).

Detalhes do Livro: Página dedicada com imagem, descrição e opções para alugar ou devolver.

Busca de Livros: Funcionalidade de busca (em desenvolvimento).

Empréstimos e Devoluções
Alugar Livro:

Reduz a quantidade disponível no estoque.

Envia um e-mail para o usuário com a data de empréstimo e devolução.

Devolver Livro:

Retorna o livro ao estoque.

Histórico de Empréstimos: Exibe informações sobre livros alugados e datas de devolução.

Interface Intuitiva
Design Responsivo: Interface amigável e adaptada para diferentes dispositivos.

Navegação Simples: Botões de "Sair" e "Voltar" para facilitar a usabilidade.

Tecnologias Utilizadas
Django: Framework Python para desenvolvimento web.

HTML/CSS: Para a estruturação e estilização das páginas.

Python: Linguagem de programação principal.

Banco de Dados: SQLite (padrão do Django) para armazenamento de dados.

Bibliotecas:

django-crispy-forms: Para formulários estilizados.

Pillow: Para manipulação de imagens dos livros.

django-environ: Para gerenciamento de variáveis de ambiente (opcional).

E-mail: Integração com serviços de e-mail para notificações de empréstimo e devolução.

Como Executar o Projeto
Pré-requisitos
Python: Certifique-se de ter o Python instalado. Caso não tenha, baixe e instale a partir do site oficial.

Django: Instale o Django utilizando o pip:

bash
Copy
pip install django
Dependências: Instale as dependências do projeto a partir do arquivo requirements.txt:

bash
Copy
pip install -r requirements.txt
Passos para Execução
Clone o repositório:

bash
Copy
git clone https://github.com/seu-usuario/biblioteca-virtual.git
cd biblioteca-virtual
Configure o banco de dados:

Execute as migrações para criar as tabelas no banco de dados:

bash
Copy
python manage.py migrate
Crie um superusuário (opcional):

Para acessar a área administrativa do Django e adicionar livros:

bash
Copy
python manage.py createsuperuser
Execute o servidor:

bash
Copy
python manage.py runserver
Acesse o projeto:

Abra o navegador e acesse:

Copy
http://127.0.0.1:8000/
