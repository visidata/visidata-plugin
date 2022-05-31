'''{{cookiecutter.description}}'''

__author__ = '{{cookiecutter.author_name}} < {{cookiecutter.github_email}} >'
__version__ = '{{cookiecutter.initial_version}}'

vd.option('disp_hello', 'Hello world!', 'string to display for hello-world command')

BaseSheet.addCommand('0', 'hello-world', 'status(options.disp_hello)')
