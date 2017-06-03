Primero: Dependencias pip
pip install -r requirements.txt


ejemplo requirements.txt
BeautifulSoup==3.2.0
Django==1.3
Fabric==1.2.0
Jinja2==2.5.5
PyYAML==3.09

pip install virtualenv -----> instala virtual environment.

virtualenv --version

$ cd my_project_folder
$ virtualenv my_project

O bien:
virtualenv -p /usr/bin/python2.7 my_project

Como saber donde esta python cuando lo ejecutamos:

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

O se puede cambiar, de manera global en el bashrc ~/.bashrc:

$ export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7


Para empezar a usar Venv:

source my_project/bin/activate

instalar paquetes:

pip install requests

Salir de venv:
deactivate

Running virtualenv with the option --no-site-packages will not include the packages that are installed globally. This can be useful for keeping the package list clean in case it needs to be accessed later. [This is the default behavior for virtualenv 1.7 and later.]
In order to keep your environment consistent, it’s a good idea to “freeze” the current state of the environment packages. To do this, run

$ pip freeze > requirements.txt

 pip install -r requirements.txt

What problem does virtualenv solve? If you like Python as much as I do, chances are
you want to use it for other projects besides Flask-based web applications.  But the
more projects you have, the more likely it is that you will be working with different
versions of Python itself, or at least different versions of Python libraries. Let’s face it:
quite often libraries break backwards compatibility, and it’s unlikely that any serious
application will have zero dependencies.  So what do you do if two or more of your
projects have conflicting dependencies?
Virtualenv  to  the  rescue!   Virtualenv  enables  multiple  side-by-side  installations  of
Python, one for each project.  It doesn’t actually install separate copies of Python, but
it does provide a clever way to keep different project environments isolated. Let’s see
how virtualenv works.
If you are on Mac OS X or Linux, chances are that the following command will work
for you:

$ pip install virtualenvwrapper

o bien para windows:

$ pip install virtualenvwrapper-win


export WORKON_HOME=$HOME/.virtualenvs
export MSYS_HOME=/c/msys/1.0
source /usr/local/bin/virtualenvwrapper.sh
or:
export WORKON_HOME=$HOME/.virtualenvs
export MSYS_HOME=C:\msys\1.0
source /usr/local/bin/virtualenvwrapper.sh


Add three lines to your shell startup file (.bashrc, .profile, etc.) to set the location where the virtual environments should live, the location of your development project directories, and the location of the script installed with this package:

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh

Lazy Loading
An alternative initialization script is provided for loading virtualenvwrapper lazily. Instead of sourcing virtualenvwrapper.sh directly, use virtualenvwrapper_lazy.sh. If virtualenvwrapper.sh is not on your $PATH, set VIRTUALENVWRAPPER_SCRIPT to point to it.

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
source /usr/local/bin/virtualenvwrapper_lazy.sh


Run: workon
A list of environments, empty, is printed.
Run: mkvirtualenv temp
A new environment, temp is created and activated.
Run: workon
This time, the temp environment is included.


Location of Environments
The variable WORKON_HOME tells virtualenvwrapper where to place your virtual environments. The default is $HOME/.virtualenvs. If the directory does not exist when virtualenvwrapper is loaded, it will be created automatically.

Location of Project Directories
The variable PROJECT_HOME tells virtualenvwrapper where to place your project working directories. The variable must be set and the directory created before mkproject is used.

https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html

///////////////////////////////////////////
Ejemplo de funcionamiento, crea un venv llamado env1 y luego se pone a trabajar en el:
$ mkvirtualenv env1
New python executable in env1/bin/python
Installing setuptools.............................................
..................................................................
..................................................................
done.
(env1)$ $ workon env1
(env1)$ lssitepackages
setuptools-0.6.10-py2.6.egg     pip-0.6.3-py2.6.egg
easy-install.pth     


///////////////////////////////////////////
Para multiples proyectos en un solo virtual environment:
mkproject myproject


///////////////////////////////////////////
virtualenv-burrito
Todo en uno, virtualenv + virtualenvwrapper

autoenv
Cuando te moves a un directorio q tiene un .env, autoenv automagicamente cambia a ese entorno virtual.

OSX:
$ brew install autoenv

Linux:
$ git clone git://github.com/kennethreitz/autoenv.git ~/.autoenv
$ echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc
