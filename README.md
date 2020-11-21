
# Bones
A cluster of 3 raspberry pi nicknamed "Bones". Bones provides CI/CD, storage, and network services for my cluster.

## TODOS:
- Create issues for these:
- Add asynchronous points for tasks that can run concurrently. (https://docs.ansible.com/ansible/latest/user_guide/playbooks_async.html)
- Use async wait_for reboot pattern found in pihole role.
- Use handlers & notify combination
- Create Jinja2 template files instead of using replace/lineinfile. (https://jinja.palletsprojects.com/en/2.11.x/templates/)

## Prerequisites

### Hardware
* Raspberry Pi 4 (minimum of 1)
* Class 10 SD Card(s)
* The group_vars folder (without this folder, the configuration will use defaults or invalid settings and will fail.)

### Software

* [Ubuntu 20 (64-bit)](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#1-overview) (installed on each Raspberry Pi)
* Custom Raspberry Pi cloud-config user-data script has been added before booting for the first time, wait a bit because it also updates/upgrades them all the way.

* Raspberry Pis need static IPs

* Ability to SSH into all Raspberry Pis and escalate privileges with sudo

* [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) 2.7.1 or higher

### Recommendations

* Setup SSH key pairs so your password is not required every time Ansible runs
* Update/Upgrade the ubuntu host before standing up the cluster. (applied in the user-data file)

#### Scripts

``` bash
# skip this step if ssh keys are already provided.
ansible-playbook -i inventory cluster.yaml
```


## Standing up Services
1. Image the raspberry pi with ubuntu 20 64bit. Copy over the custom user-data script.
2. On first boot, the custom user-data script will update and install all packages, this may take some time (default password is ubuntu)
3. Fetch configuration files: the group_vars folder and ansible.cfg must be present and configured to your liking.
4. Test ansible: Check if ansible can reach your services after setting up ssh-keys.

``` bash
ansible -m ping all
```
5. Deploy: `ansible-playbook cluster.yml`

## working with Esp8266
- The esp8266 role doesnt really work on esp8266, it'll create a raspberrypi with a viable enviornment with which to develop on esp8266s.
- use the makefile commands to manipulate esp8266 projects.
- prepare a connected esp8266 `make dependencies flash`
- connect to serial port of esp8266 `make connect`
- [web repl link here](http://micropython.org/webrepl/#192.168.0.146:8266/) * IP might be wrong.
- find your webrepl daemon on the serial line after rebooting with control + d an esp8266
## References & Credits
These playbooks were assembled using a handful of very helpful guides:
* [ansible-rpi-pihole](https://github.com/gsemet/ansible-rpi-pihole) useful ansible techniques.
* [ansible-pi](https://github.com/motdotla/ansible-pi) useful ansible tools for raspberry pi.
* [**rak8s**](https://rak8s.io) the source of this fork
* [ansible-raspberry-pi-kubernetes](https://github.com/aporcupine/ansible-raspberry-pi-kubernetes) helpful repository and articles
* [Opensource Raspberry Pi Kubernetes Article](https://opensource.com/article/20/6/kubernetes-raspberry-pi#:~:text=%20Build%20a%20Kubernetes%20cluster%20with%20the%20Raspberry,the%20Kubernetes%20packages%20installed%2C%20you%20can...%20More%20)