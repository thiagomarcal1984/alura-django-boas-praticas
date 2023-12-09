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
