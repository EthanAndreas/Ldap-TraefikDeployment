# LdapServer

## Usage

- Install ansible and requirements
```bash
pip install ansible
pip install -r requirements.txt
```
Do not use docker apt package, use the one from python

- Add user to docker group
```bash
sudo usermod -aG docker $USER
exec su -l $USER
```

- Install ldap
```bash
sudo apt install ldap-utils
```

- Install apache2
```bash
sudo apt install apache2
```

- Run playbook
```bash
sh start.sh
```

## Remark