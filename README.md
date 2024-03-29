# O que é Django?
O Django é um framework content-driven (orientado a conteúdo). É um framework bom para sites de notícias, fóruns e blogs.

O framework foi criado para atender a demandas de um jornal de notícias do estado do Kansas.

O nome do framework é uma homenagem ao guitarrista de jazz Django Reinhardt.

O frontend e o backend ficam no mesmo projeto do Django (o que o torna um framework fullstack).

# Virtualenv
Como criar uma virtualenv de acordo com o curso (`virtualenv venv`):
```
PS D:\alura\django-boas-praticas> virtualenv venv
created virtual environment CPython3.8.8.final.0-64 in 6187ms
  creator CPython3Windows(dest=D:\alura\django-boas-praticas\venv, clear=False, no_vcs_ignore=False, global=False)      
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Thiago\AppData\Local\pypa\virtualenv)
    added seed packages: pip==21.0.1, setuptools==54.1.2, wheel==0.36.2
  activators BashActivator,BatchActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
PS D:\alura\django-boas-praticas> 
```

Checando a versão da virtualenv com `virtualenv --version`:
```
PS D:\alura\django-boas-praticas> virtualenv --version
virtualenv 20.4.3 from c:\users\thiago\appdata\local\programs\python\python38\lib\site-packages\virtualenv\__init__.py
PS D:\alura\django-boas-praticas> 
```
> Eu prefiro criar uma virtualenv com o seguinte comando:
> ```
> PS D:\alura\django-boas-praticas> python -m venv venv
> PS D:\alura\django-boas-praticas> 
> ```

Ativando um ambiente virtual no Windows: 
```
PS D:\alura\django-boas-praticas> .\venv\Scripts\activate
(venv) PS D:\alura\django-boas-praticas> 
```

Atualização do gerenciador de pacotes `pip` no Windwos:
```
(venv) PS D:\alura\django-boas-praticas> python -m pip install --upgrade pip  
Requirement already satisfied: pip in d:\alura\django-boas-praticas\venv\lib\site-packages (22.3)
Collecting pip
  Using cached pip-23.3.1-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.3
    Uninstalling pip-22.3:
      Successfully uninstalled pip-22.3
Successfully installed pip-23.3.1
(venv) PS D:\alura\django-boas-praticas> 
```

Instalando a dependência do Django com `pip`:
```
(venv) PS D:\alura\django-boas-praticas> pip install django==4.1
Collecting django==4.1
  Downloading Django-4.1-py3-none-any.whl (8.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.1/8.1 MB 9.6 MB/s eta 0:00:00
Collecting asgiref<4,>=3.5.2 (from django==4.1)
  Using cached asgiref-3.7.2-py3-none-any.whl.metadata (9.2 kB)
Collecting sqlparse>=0.2.2 (from django==4.1)
  Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
Collecting tzdata (from django==4.1)
  Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)
Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.7.2 django-4.1 sqlparse-0.4.4 tzdata-2023.3
(venv) PS D:\alura\django-boas-praticas> 
```

# Servidor
Como ver as dependências instaladas no ambiente virtual com `pip freeze`:
```
(venv) PS D:\alura\django-boas-praticas> pip freeze
asgiref==3.7.2
Django==4.1
sqlparse==0.4.4
tzdata==2023.3
(venv) PS D:\alura\django-boas-praticas> 
```

> A boa prática é jogar o conteúdo do `pip freeze` para um arquivo chamado `requirements.txt` (comando: `pip freeze > requirements.txt`).
> Depois, para instalar as dependências, use o comando `pip install -r requirements.txt`.

## Comandos do Django
O Django possui o comando `django-admin help` para mostrar os comandos disponiveis na CLI:
```
(venv) PS D:\alura\django-boas-praticas> django-admin help

Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
Note that only Django core commands are listed as settings are not properly 
configured (error: Requested setting INSTALLED_APPS, but settings are not 
configured. You must either define the environment variable 
DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.).
(venv) PS D:\alura\django-boas-praticas> 
```
Para criar um projeto Django chamado `setup`, use o comando `django-admin startproject setup .`. Repare que há um ponto depois do nome do projeto. Isso é bom para que a estrutura do projeto fique mais simples (pasta do projeto `setup` e o arquivo `manage.py`). Assim não é criada uma pasta pai chamada `setup` que contenha as duas macro-estruturas geradas (a pasta do aplicativo `setup` e o arquivo `manage.py`).

> Uma boa prática para criar projetos Django é batizá-los com o nome de `config` ou `setup`, porque nesse projeto se concentram as configurações da aplicação Django como um todo.

Agora já temos uma estrutura pronta para rodar a aplicação. Para isso, execute o comando `python manage.py runserver`: 
```
(venv) PS D:\alura\django-boas-praticas> python .\manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly 
until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
December 09, 2023 - 12:33:31
Django version 4.1, using settings 'setup.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

# Para saber mais: tipos de ambientes virtuais

A utilização de ambientes virtuais em projetos Python é uma prática padrão no desenvolvimento de software com a linguagem. O consenso da comunidade Python de que ambientes virtuais são uma ótima prática levou à criação de vários projetos com o objetivo de oferecer versões alternativas de ambientes virtuais e novas formas de gerenciá-los.

A seguir temos alguns exemplos de ambientes virtuais e ferramentas relacionadas mais utilizadas no mercado:

- `venv` (https://docs.python.org/pt-br/3/library/venv.html): É o ambiente virtual “padrão” do Python e sua grande vantagem é já vir instalado como um módulo na linguagem a partir da versão 3.3. Se trata de um subset (parte menor) da ferramenta **virtualenv**.
- `Virtualenv` (https://virtualenv.pypa.io/en/latest/): É uma ferramenta feita especificamente para a criação de ambientes virtuais e precede a criação da **venv**, sendo um superset (parte maior) dela. Algumas de sua principais vantagens sobre a **venv** são:
  - Maior velocidade, graças ao método `app-data` seed;
  - Pode criar ambientes virtuais para versões arbitrárias do Python instaladas na máquina;
  - Pode ser atualizado utilizando a ferramenta **pip**;
  - Possui uma *Programmatic API*, capaz de descrever um ambiente virtual sem criá-lo.
- `Conda` (https://docs.conda.io/en/latest/): É uma alternativa não apenas às ferramentas de ambiente virtuais já citadas, mas ao instalador de pacotes pip também. Possui um escopo mais centrado na área de ciência de dados e possui a capacidade de instalar pacotes fora do ecossistema do Python.
- `Virtualenvwrapper` (https://virtualenvwrapper.readthedocs.io/en/latest/): É uma extensão do projeto **Virtualenv** que torna a criação, deleção e gerenciamento geral dos ambientes virtuais mais fácil. Uma grande vantagem de sua utilização é a organização de todos os ambientes virtuais utilizados em um só lugar, além de facilitar os comandos de CLI.
- `Poetry` (https://python-poetry.org/): É uma ferramenta para gerenciamento de dependências e pacotes do Python. Através do Poetry é possível declarar quais pacotes um projeto necessita para funcionar, de forma parecida ao `requirements.txt`, porém, de forma determinística.

# Para saber mais: princípios do Django
- produtividade;
- documentação;
- código limpo.

A questão dos frameworks web do século XXI é tornar o desenvolvimento web mais rápido. E é isso que o Django deve permitir, um desenvolvimento muito veloz.

Aplicações Django devem usar o mínimo possível de código, sem haver código padrão. Django deve aproveitar as características dinâmicas do Python, como introspecção (https://pt.wikipedia.org/wiki/Introspec%C3%A7%C3%A3o_%28computa%C3%A7%C3%A3o%29).

Caso queira saber mais sobre a Filosofia do Django segundo a documentação oficial: https://docs.djangoproject.com/pt-br/4.1/misc/design-philosophies/

# Idioma e timezone
A configuração do idioma e da timezone é feita no arquivo `settings.py`, localizada no diretório do projeto principal da aplicação:
```
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'
```
> A biblioteca para implementação da timezone do Django mudou de `pytz` para `zoneinfo`.

# Variáveis de ambiente
Vamos instalar o `python-dotenv` para usarmos variáveis de ambiente:
```
(venv) PS D:\alura\django-boas-praticas> pip install python-dotenv
Collecting python-dotenv
  Downloading python_dotenv-1.0.0-py3-none-any.whl (19 kB)
Installing collected packages: python-dotenv
Successfully installed python-dotenv-1.0.0
```
Depois, incluímos algumas configurações no arquivo `settings.py`:

```python
from pathlib import Path, os
from dotenv import load_dotenv

load_dotenv() # Esta função vai carregar o arquivo `.env` do projeto
# Resto do código

SECRET_KEY = str(os.getenv('SECRET_KEY')) 
# Garanta que o conteúdo da SECRET_KEY será carregado como string.
```

> Criei o arquivo `exemplo.env` para conter os parâmetros que serão carregados como variáveis de ambiente, uma vez que o arquivo `.env` é ignorado pelo `.gitignore`.

# Git e GitHub
Se você visitar o endereço http://gitignore.io, você pode usar o gerador de `.gitignore` deles. Basta escolher as linguagens que serão usadas no seu código e copiar o `.gitignore` criado.

# App e projeto
App é uma aplicação que roda sobre o projeto (no nosso caso, é o diretório `setup`).

Vamos criar um app de galeria com o comando `python .\manage.py startapp galeria`.

Os seguintes seis arquivos do diretório `galeria` (além do diretório migrations) serão criados:
- `__init__.py`;
- admin.py;
- apps.py;
- models.py;
- tests.py;
- views.py.

# Views e URLs
No arquivo `views.py` definimos o que será exibido no navegador. Para isso, definimos funções de view nesse arquivo.

Alterações no arquivo `galerias/views.py`:
```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('''
      <h1>Alura Space</h1><p>Bem vindo ao espaço!</p>
    ''')
```

Uma vez que a view foi definida, é necessário roteá-la no arquivo `urls.py` do projeto principal

Alterações no arquivo `setup/urls.py`:
```python
from django.contrib import admin
from django.urls import path

from galeria.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
```
> Repare na lista `urlpatterns`: originalmente só tinha uma rota/path para o painel administrativo. Agora, a raiz da aplicação (representada pela string vazia) redireciona para a view `index`, que está no pacote `galeria.views`.

# Isolando as URLs
Para isolar as urls associadas a cada aplicativo, crie um arquivo `urls.py` para cada aplicativo e os referencie no arquivo `urls.py` do projeto principal por meio da função `include('nome_do_app.urls')`

Criação do arquivo `galeria/urls.py`:
```python
from django.urls import path

from galeria.views import index

urlpatterns = [
    path('', index),
]
```

Alterações no arquivo `setup/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
]
```
> Note que o import da view index foi removida deste arquivo, pois é o arquivo `galeria/urls.py` que vai indicar quais visões serão exibidas.
>
> Note também que não importamos um pacote na função `include`: apenas fornecemos uma string com o endereço do módulo urls do aplicativo (no exemplo, `galeria.urls`).

# Templates
Para dinamizar a geração das páginas, podemos usar os templates.

Para usá-los, precisamos configurar o diretório onde eles ficarão armazenados para renderização posterior.

Alterações no arquivo `setup/settings.py`:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # O parâmetro 'DIRS' contém uma lista dos diretórios onde
        # estarão os templates que serão renderizados pelo projeto.
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
          # Resto do código
        }
    }
]
```

Os templates são chamados da view por meio da função `render`.

Mudanças no arquivo `galeria.views.py`:
```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

# Carregando o template
Nesta aula, vamos apenas criar um diretório para os templates do aplicativo da galeria.

Mudança no arquivo `galeria/views.py`:
```python
from django.shortcuts import render

def index(request):
    # return render(request, 'index.html')
    return render(request, 'galeria/index.html')
```

# Arquivos estáticos
Primeiro: configurar 3 variáveis no arquivo `settings.py`:
1. `STATIC_URL` já é escrita por padrão pelo `django-admin`. Seu valor é `static/`;
2. `STATIC_ROOT` é o caminho do diretório onde estarão os arquivos obtidos do comando `python manage.py collectstatic`.
3. `STATICFILES_DIR` é uma lista com todos os diretórios de onde estarão os arquivo que serão compilados para o caminho mencionado em `STATIC_ROOT`.

Mudanças no arquivo `settings.py`:
```python
# Resto do código
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    # Arquivos-fonte  para compilação posterior para
    # o diretório STATIC_ROOT.
    os.path.join(BASE_DIR, 'setup/static'), 
]

# Caminho absoluto de onde buscamos os arquivo estáticos coletados.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Resto do código
```

Mas... apenas configurar os diretórios em settings.py não basta. É necessário carregar o aplicativo `static` no template. Os comando no template são sempre embedados com `{% %}`.

Dentro da página `galeria/index.html` iremos carregar o aplicativo `static` e usar sua função para buscar os arquivos armazenados em `STATIC_ROOT`.

Mudanças no arquivo `galeria/index.html`:
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <!-- Resto do código -->
    <link rel="stylesheet" href="{% static '/styles/style.css' %}">
</head>

<body>
  <!-- Resto do código -->
```
> Repare que no início carregamos o aplicativo `static` com o comando `{% load static %}`, e que para carregarmos a folha de estilos salva em `STATIC_ROOT` usamos o comando `{% static 'nome_do_arquivo_estatico' %}`.

# Carregando as imagens
Nesta aula apenas configuramos as tags de imagem para carregar os arquivos estáticos com o comando `{% static 'nome_do_arquivo_estático' %}`.

Destaque para o uso da tecla `Alt` do Windows para posicionar vários cursores no VS Code.

# Outras páginas
Vamos criar um HTML chamado `imagem.html`. Nele vamos novamente carregar o aplicativo `static` e as imagens/folha de estilo serão carregadas usando o comando `{% static 'nome_do_arquivo_estatico' %}`:

```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <!-- Resto do código -->
    <link rel="stylesheet" href="{% static 'styles/style.css' %}">
</head>

<body>
    <div class="pagina-inicial">
        <header class="cabecalho">
            <!-- Carregando o logotipo estático -->
            <img src="{% static '/assets/logo/Logo(2).png' %}" alt="Logo da Alura Space" />
            <div class="cabecalho__busca">
                <div class="busca__fundo">
                    <input class="busca__input" type="text" placeholder="O que você procura?">
                    <!-- Carregando o ícone estático -->
                    <img class="busca__icone" src="{% static '/assets/ícones/1x/search.png' %}" alt="ícone de search">
                </div>
            </div>
        </header>
        <!-- Resto do código -->
```

Depois de criada a página, criaremos um função de view para ela no arquivo `galeria/views.py`:
```python
from django.shortcuts import render

# Resto do código

def imagem(request):
    return render(request, 'galeria/imagem.html')
```

Finalmente, vamos configurar as rotas do Django no arquivo `galerias/urls.py`:
```python
from django.urls import path

from galeria.views import index, imagem

urlpatterns = [
    path('', index),
    path('imagem', imagem),
]
```
# URL name
Podemos nomear/rotular cada rota configurada no arquivo `urls.py`. Basta acrescentar para a função `path` de cada rota o parâmetro `name='nome_da_rota'`.

Mudanças no arquivo `galeria/urls.py`:
```python
from django.urls import path

from galeria.views import index, imagem

urlpatterns = [
    # A rota raiz foi batizada de "index".
    path('', index, name='index'), 
    # A rota /imagem foi batizada de "imagem".
    path('imagem', imagem, name='imagem'), 
]
```

Pra que nomeamos as rotas? Para referenciá-las por meio do comando `{% url 'nome_da_rota' %}`.

Veja o exemplo no arquivo `templates/galeria/imagem.html`:
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <!-- Resto do código -->

</head>

<body>
    <div class="pagina-inicial">
        <!-- Resto do código -->
        <main class="principal">
            <section class="menu-lateral">
                <nav class="menu-lateral__navegacao">
                    <!-- Aqui inserimos um comando {% url 'nome_da_rota' %} -->
                    <a href="{% url 'index' %}"><img src="{% static '/assets/ícones/1x/Home - ativo.png' %}"> Home</a>
                    <!-- Resto do código -->
```
> Se você tentar acessar o HTML do template diretamente ao invés de usar o comando `{% url 'rota' %}`, o Django não vai conseguir carregar a view corretamente.

# Base e DRY
O Django utiliza um conceito de extensão de templates a partir da definição de blocos de conteúdo.

Para atender ao princípio do DRY (Don't Repeat Yourself), podemos criar um template-base e nele incluir os conteúdos que podem se repetir (por exemplo, o cabeçalho HTML das páginas).

A estrutura de um template-base é semelhante ao seguinte código:
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">

<head>
  <!-- Conteúdo do head -->
</head>
<body>
  {% block content %}
  {% endblock %}
</body>
</html>
```
Observações: 
1. O comando `{% load static %}` não é obrigatório, mas como o cabeçalho costuma ter conteúdo estático (CSS, JavaScript etc.), precisamos carregá-lo usando a função `{% static 'arquivo' %}` do aplicativo `static`.
2. O comando `{% block content %}` define um bloco cujo nome é `content`. Podemos criar vários blocos com diferentes nomes.
3. Todo block precisa ser fechado com o comando `{% endblock %}`.

E sempre que um template-base for reusado, usamos o comando de importação `{% extends 'nome_do_arquivo_de_template_base' %}`.

Por exemplo, no arquivo `galeria/index.html`:
```html
{% extends 'galeria/base.html' %}
{% load static %}
{% block content %}
  <header class="cabecalho">
    <h1>Aqui fica o conteúdo de galeria/index.html</h1>

    <img src="{% static '/assets/logo/Logo(2).png' %}" />
  </header>
  <!-- Resto do código -->
{% endblock %}
```
Observações:
1. O comando `{% extends 'galeria/base.html' %}` serve para dizer que o template atual precisa ser incorporado (estender) ao template base que está no arquivo `galeria/base.html`;
2. Novamente, o comando `{% load static %}` não é obrigatório, exceto se você precisar carregar conteúdo estático (o que é o caso, por causa das imagens estáticas).
3. Os comandos `{% block content %}` e `{% endblock %}` estabelecem onde o bloco chamado `content` começa e termina. Dentro desse bloco colocamos o conteúdo específico do template atual.

# Partials
Partials são conteúdos que podem ser reusados nos templates. Por convenção, os arquivos de partials são guardados no diretório `partials` e são prefixados com um underline.

O menu lateral é um exemplo de partial que pode ser definido. Chamaremos o arquivo de `galeria/partials/_menu-lateral.html`:
```html
{% load static %}
<section class="menu-lateral">
    <nav class="menu-lateral__navegacao">
        <a href="{% url 'index' %}"><img src="{% static '/assets/ícones/1x/Home - ativo.png' %}"> Home</a>
        <a href="#"><img src="{% static '/assets/ícones/1x/Mais vistas - inativo.png' %}"> Mais vistas</a>
        <a href="#"><img src="{% static '/assets/ícones/1x/Novas - inativo.png' %}"> Novas</a>
        <a href="#"><img src="{% static '/assets/ícones/1x/Surpreenda-me - inativo.png' %}"> Surpreenda-me</a>
    </nav>
</section>
```
> Note mais uma vez que, como o menu usa arquivos estáticos, é necessário usar o aplicativo `static`, carregando-o com o comando `{% load static %}`.

Para aplicar uma partial, usamos o comando `{% include 'dir/partial/_arquivo' %}`. Por exemplo, em `index.html`:
```html
{% extends 'galeria/base.html' %}
{% load static %}
{% block content %}
  <div class="pagina-inicial">
      <!-- Resto do código de galeria/index.html -->
      <main class="principal">
          {% include 'galeria/partials/_menu-lateral.html' %}
      </main>
  </div>
{% endblock %}
```

Outro exemplo é com a partial para o rodapé, que chamaremos de `galeria/partials/_footer.html`:
```html
{% load static %}
<footer class="rodape">
    <div class="rodape__icones">
        <a href="https://twitter.com/AluraOnline">
            <img src="{% static '/assets/ícones/1x/twitter.png' %}">
        </a>
        <a href="https://www.instagram.com/aluraonline/">
            <img src="{% static '/assets/ícones/1x/instagram.png' %}">
        </a>
    </div>
    <p class="rodape__texto">Desenvolvido por Alura</p>
</footer>
```

Vamos incluir a partial do footer em `galeria/base.html`:
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <!-- Resto do head -->
</head>

<body>
    {% block content %}
    {% endblock %}
    {% include 'galeria/partials/_footer.html' %}
</body>

</html>
```
