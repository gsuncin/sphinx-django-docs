# Projeto criado em reuniao e apresentacao 14/08/2024 com a equipe de Devs, UX e QA

# Como utilizar

1. Instalar os pacotes -> django-docs | Django | sphinx | sphinx-rtd-theme
2. Criar diretorio docs e acessado via cd (prompt de comando)
3. Executar sphinx-quickstart
4. Alterar arquivo conf.py com configuracao do Django
5. Executar sphinx-apidoc -o source ../ (source apenas se tiver escolhido para separar build e source ao rodar sphinx-quickstart)
6. Limpar infos desnecessarias, incluir no Index módulos
7. Executar make html (make do sphinx gerado no quickstart)


# Caso queira isolar do Django, basta executar:
    $ rm -rf api
    $ rm -rf core
    $ rm manage.py
    $ docker compose up -d --build (irá usar o nginx para rodar a documentacao na porta 80 da maquina)

# Referencias
    guia geral usado https://medium.com/free-code-camp/sphinx-for-django-documentation-2454e924b3bc
    fonte: https://www.sphinx-doc.org/en/master/examples.html
    https://www.writethedocs.org/


# Exemplos
    https://flask.palletsprojects.com/en/3.0.x/
    https://www.writethedocs.org/
    https://www.kernel.org/doc/html/latest/index.html

# arquivo conf.py
``` python
    # Configuration file for the Sphinx documentation builder.
    #
    # For the full list of built-in configuration values, see the documentation:
    # https://www.sphinx-doc.org/en/master/usage/configuration.html

    # -- Project information -----------------------------------------------------
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


    import os # Incluido
    import sys # Incluido
    sys.path.insert(0, os.path.abspath('../..')) # Incluido

    project = 'Docs'
    copyright = '2024, ITMSS'
    author = 'ITMSS'
    release = '0.1'

    # -- General configuration ---------------------------------------------------
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

    extensions = [
        "sphinx.ext.autodoc", # Incluido
        "sphinx.ext.napoleon", # Incluido
        "sphinx_autodoc_typehints", # Incluido
        "sphinx.ext.viewcode",  # Incluido

    ]

    templates_path = ['_templates']
    exclude_patterns = [
        "migrations/*", # Incluido
        "*/admin.py", # Incluido
        "*/apps.py",    # Incluido
        "*/models.py", # Incluido
        "*/urls.py", # Incluido
    ]



    # -- Options for HTML output -------------------------------------------------
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

    # html_theme = 'alabaster' Padrao
    html_theme = 'sphinx_rtd_theme'
    html_static_path = ['_static']

    autodoc_mock_imports = [
        "django.contrib.admin",
        "django.apps",
        "django.db.migrations"
    ]
```