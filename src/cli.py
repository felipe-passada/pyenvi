import click
import subprocess

@click.command()
@click.argument("os")
def cli(os):
  """
    This Script helps you to prepare and configure your environment
  """
  languages = 'nodejs, java'
  click.echo('### Env setup tool ###')

  if (os.casefold() == "Fedora".casefold()):
    configure_install_fedora()

def configure_install_fedora(): 
  subprocess.run(['sudo', 'dnf', 'install', 'htop'])

def configure_install_mac_os():
  subprocess.run([])


if __name__ == "__cli__":
   cli()