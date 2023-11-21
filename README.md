# LadpServver

## Usage
```bash
pip install ansible
pip install -r requirements.txt
sudo usermod -aG docker $USER
exec su -l $USER
ansible-playbook -i inventory.yaml playbook_tpl.yaml
```