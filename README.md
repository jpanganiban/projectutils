#Project Utils

Tired of repeating myself.

##Installation

    # virtualenv
    python setup.py install

    # system install
    sudo python setup.py install

    # develop install
    python setup.py develop

##Bootstrap

Creates project skeleton.

    bootstrap.project [project name]

Structure

    /[project name]
        - /[project name as package]
            - __init__.py
        - .gitignore
        - requirements
        - setup.py

###TODO:

1) Bootstrap for specific projects (web/django, web/flask, module, package).
2) Bootstrap for projects in a different language (C/C++, Ruby, Javascript, etc)
