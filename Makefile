PUB:=$$(cat /c/Users/Deet/.ssh/id_rsa.pub)
PRI:=$$(cat /c/Users/Deet/.ssh/id_rsa)
PLAYBOOK=cluster.yaml

build:
	docker build --build-arg ssh_prv_key="$(PRI)" --build-arg ssh_pub_key="$(PUB)"  -t local/ansible .

run:
	docker run -it --rm --name ansible local/ansible $(PLAYBOOK)