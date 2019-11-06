# Ansible to manage laptop

Manage my laptop how I want it - so I don't have to keep doing this manually.
Combine with [dotfiles](https://github.com/bdellegrazie/dotfiles)

## Prerequisites

* It is assumed this is being run from the target laptop, although the code will work remotely
* [dotfiles](https://github.com/bdellegrazie/dotfiles) install process should have already been executed
* pipenv should be installed, using pipx (`pipx install pipenv`)
* If using [DisplayLink drivers](https://www.displaylink.com/downloads), download the driver first and put it in ~/Downloads as the driver is behind an "accept license" page.
  However, it has caused problems with the NVidia binary drivers, so prefer DisplayPort instead

## Execution

1. Change to this repo's directory
2. Adjust inventory, uncommenting or commenting out localhost as desired
3. Install prerequisites into auto generated venv: `pipenv install`
4. Run Ansible: `pipenv run ansible-playbook -i inventory -K site.yml`
