
# Metal
* Repository forked from [**rak8s**](https://github.com/rak8s).
* [**rak8s**](https://github.com/rak8s) is maintained by [Chris Short](https://github.com/chris-short) and a community of open source folks willing to help.

## Services:
- automatically deployed: NONE.

## Prerequisites
### Router Config:
- StaticIPs for all the devices
- MetalLB needs 200-220 to expose services
- Port forward 80 and 443 to the Ingress-Controller's exposed port.

### Hardware

* Raspberry Pi 4 (2 or more)
* Class 10 SD Cards
* Network connection (wireless or wired) with access to the internet
* The group_vars folder (without this folder, the configuration will use defaults or invalid settings and will fail.)

### Software

* [Ubuntu 20 (64-bit)](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#1-overview) (installed on each Raspberry Pi)

* Custom Raspberry Pi cloud-config user-data script has been added before booting for the first time, wait a bit because it also updates/upgrades them all the way.

* Raspberry Pis should have static IPs
    * Requirement for Kubernetes and Ansible inventory
    * You can set these via OS configuration or DHCP reservations (your choice)

* Ability to SSH into all Raspberry Pis and escalate privileges with sudo
    * The pi user is fine
    * Please change the pi user's password

* [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) 2.7.1 or higher

* [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/) should be available on the system you intend to use to interact with the Kubernetes cluster.
    * If you are going to login to one of the Raspberry Pis to interact with the cluster `kubectl` is installed and configured by default on the master Kubernetes master.
    * If you are administering the cluster from a remote machine (your laptop, desktop, server, bastion host, etc.) `kubectl` will not be installed on the remote machine but it will be configured to interact with the newly built cluster once `kubectl` is installed.

### Recommendations

* Setup SSH key pairs so your password is not required every time Ansible runs
* Update/Upgrade the ubuntu host before standing up the cluster. () 

#### Scripts
* In order to execute the scripts new hosts should first be added to the "new" group in the inventory
* Password is ubuntu, the custom user-data file prevents the default password from expiring.
* On first boot, the custom user-data script will update and install all packages, this may take up to 10 minutes.

``` bash
ansible-playbook -i inventory util/setup-ssh-keys.yml --ask-become-pass --ask-pass -u ubuntu
```
    
``` bash
ansible-playbook -i inventory util/setup-ubuntu.yml
```

## Stand Up Your Kubernetes Cluster

### Download the latest release or clone my fork of rak8s:

``` bash
git clone https://github.com/GGonryun/rak8s.git
```

### Modify ansible.cfg and inventory

Modify the `inventory` file to suit your environment. Change the names to your liking and the IPs to the addresses of your Raspberry Pis.

If your SSH user on the Raspberry Pis are not the Raspbian default `pi` user modify `remote_user` in the `ansible.cfg`.

### Confirm Ansible is working with your Raspberry Pis:

``` bash
ansible -m ping all
```

This may fail to ping if you have not setup SSH keys and only configured your Pi's with passwords

## Deploy, Deploy, Deploy

``` bash
ansible-playbook setup.yml
// if the reboots get stuck, 
//    start over to verify everything went thru fine, 
// then proceed with:
ansible-playbook plonk.yml
```

## Interact with Kubernetes

### CLI

Test your Kubernetes cluster is up and running:

``` bash
kubectl get nodes
```

The output should look something like this:

``` bash
NAME       STATUS    ROLES     AGE       VERSION
pik8s000   Ready     master    2d        v1.9.1
pik8s001   Ready     <none>    2d        v1.9.1
pik8s002   Ready     <none>    2d        v1.9.1
pik8s003   Ready     <none>    2d        v1.9.1
pik8s005   Ready     <none>    2d        v1.9.1
pik8s004   Ready     <none>    2d        v1.9.1
```

## Dashboard

rak8s installs the non-HTTPS version of the Kubernetes dashboard. This is not recommended for production clusters but, it simplifies the setup. Access the dashboard by running:

``` bash
kubectl proxy
```

Then open a web browser and navigate to:
[http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/](http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/)

## Need to start over?
1. Think about it.
2. Reimage all your stuff.
## Interacting w/ Jenkins
you can find the admin password here: `/var/lib/jenkins/secrets/initialAdminPassword` you can interact with jenkins by visiting `<node_ip>:8080`. Anything with a jenkins role in the cluster.yml file will also have a jenkins frontend.

## Jenkins Notes
1. Jenkins will need you to setup your global environments under manage jenkins => configure system => global properties => environment variables.
2. Jenkins will also need additional docker plugins.
3. Currently, we have to manually had new jenkins hosts.

## Role Descriptions
1. **Builder**: has dependencies on docker, but this docker host will now be able to build multi-architecture builds for most common environments.

## Where to Get Help

Create an issue on this github repo.

## Etymology

[**rak8s**](https://rak8s.io) (pronounced rackets - /ˈrækɪts/)

Coined by [Kendrick Coleman](https://github.com/kacole2) on [13 Jan 2018](https://twitter.com/KendrickColeman/status/952242602690129921)

## References & Credits

These playbooks were assembled using a handful of very helpful guides:

* [**rak8s**](https://rak8s.io) the source of this fork
* [kalaxy](https://github.com/christian-schlichtherle/kalaxy) helpful repository and articles
* [ansible-raspberry-pi-kubernetes](https://github.com/aporcupine/ansible-raspberry-pi-kubernetes) helpful repository and articles
* [Opensource Raspberry Pi Kubernetes Article](https://opensource.com/article/20/6/kubernetes-raspberry-pi#:~:text=%20Build%20a%20Kubernetes%20cluster%20with%20the%20Raspberry,the%20Kubernetes%20packages%20installed%2C%20you%20can...%20More%20)
* [K8s on (vanilla) Raspbian Lite](https://gist.github.com/alexellis/fdbc90de7691a1b9edb545c17da2d975) by [Alex Ellis](https://www.alexellis.io/)
* [Installing kubeadm](https://kubernetes.io/docs/setup/independent/install-kubeadm/)
* [kubernetes/dashboard - Access control - Admin privileges](https://github.com/kubernetes/dashboard/wiki/Access-control#admin-privileges)

A very special thanks to [**Alex Ellis**](https://www.alexellis.io/) and the [OpenFaaS](https://www.openfaas.com/) community for their assitance in answering questions and making sense of some errors.
