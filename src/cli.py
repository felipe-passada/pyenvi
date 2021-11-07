import click
from PyInquirer import prompt, Separator
import subprocess
"""
TODO: 
- show languages list to be installed (maybe use pyinquerer)
- show container tools to be installed eg: 'docker, kubernets, etc...'
"""
questions = [
  {
    'type': 'checkbox',
    'message': 'Select Languages',
    'name': 'languages',
    'choices': [
    Separator('= Programming Languages ='),
    {
      'name': 'NodeJs',
      'value': 'nodejs'
    },
    {
      'name': 'Java',
      'value': 'java'
    },
    {
      'name': 'Python',
      'value': 'python'
    },
  ],
  'validate': lambda answer: 'You must choose at least one topping.' \
    if len(answer) == 0 else True
  },
  {
    'type': 'checkbox',
    'message': 'Select container tools',
    'name': 'container',
    'choices': [
    Separator('= Container tooling ='),
    {
      'name': 'Docker',
      'value': 'docker'
    },
    {
      'name': 'Podman',
      'value': 'podman'
    },
    {
      'name': 'K8\'s',
      'value': 'kubernets'
    },
  ],
  'validate': lambda answer: 'You must choose at least one topping.' \
    if len(answer) == 0 else True
  }
]

@click.command()
@click.argument("os")
def cli(os):
  """
    This Script helps you to prepare and configure your environment
  """
  click.echo('### Env setup tool ###')

  # if (os.casefold() == "Fedora".casefold()):
    # configure_install_fedora(languages)
  answner = prompt(questions)
  languages, tools = answner.values()
  print("Languages to be installed: ", languages, " tools: ", tools)
  for language in languages:
    subprocess.run(['sudo', 'dnf', 'install', language])


#TODO:
# - Change this function to install_linux
# - Create a distro dictionary to match the distro an then replace the pkg-mng
# eg: `subprocess.run(['sudo', pkg-mng, 'install', languages)`
def configure_install_fedora(languages): 
  subprocess.run(['sudo', 'dnf', 'install', languages[0]])

def configure_install_mac_os():
  subprocess.run([])


if __name__ == "__cli__":
   cli()