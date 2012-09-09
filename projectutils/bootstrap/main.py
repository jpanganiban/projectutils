from jinja2 import Environment, PackageLoader
import argparse
import subprocess
import os


env = Environment(loader=PackageLoader('projectutils', 'templates'))


def write_file(variables, path, filename, template):
    with open(os.path.join(path, filename), 'w') as f:
        template = env.get_template(template)
        f.write(template.render(**variables))


def main():
    parser = argparse.ArgumentParser(description="Bootstrap Project: Project skeleton maker")
    # Project Name
    parser.add_argument('name', metavar="Project Name",
                        type=str, help="Project name")

    args = parser.parse_args()

    project = {
        'name': args.name,
    }

    current_path = os.path.abspath('.')

    # Check if project already exists.
    project_path = os.path.join(current_path, project['name'])
    if os.path.exists(project_path):
        return Exception("Project already exists.")

    project['description'] = str(raw_input("What is your project about? "))
    project['author'] = str(raw_input("What is the name of the project author? "))
    project['version'] = str(raw_input("What is your project's initial version? "))
    project['git'] = str(raw_input("Would you like to use git? [Y/N] ")).upper() == 'Y'
    if project['git']:
        project['remote'] = str(raw_input("What is your projects git remote URL? "))

    print "Making directories..."
    # Make project directory
    os.mkdir(project['name'])
    # Make project package
    os.mkdir(os.path.join(project_path, project['name']))

    print "Writing files..."
    # Make project __init__
    write_file(project, os.path.join(project_path, project['name']),
               '__init__.py', '__init__.template')
    # Make setup.py
    write_file(project, project_path, 'setup.py', 'setup.template')
    # Make readme
    write_file(project, project_path, 'README.md', 'readme.template')
    # Make gitiginore
    write_file(project, project_path, '.gitignore', 'gitignore.template')
    # Make requirements
    write_file(project, project_path, 'requirements', 'blank.template')

    # Go to project directory
    os.chdir(project_path)
    # Initialize Git if would like to use git
    if project['git']:
        subprocess.call(['git', 'init'])
        subprocess.call(['git', 'remote', 'add', 'origin', project['remote']])
        subprocess.call(['git', 'add', '-A'])
        subprocess.call(['git', 'commit', '-a', '-m', "Initial project commit"])
        if str(raw_input("Would you like to push your project now? [Y/N] ")).upper() == 'Y':
            subprocess.call(['git', 'push', 'origin', 'master'])


    print "==============================================="
    print "Project bootstrap complete."
    print "Your project name is: %s" % project['name']
    print "Your project path is: %s" % project_path
    print "==============================================="

    return 0
