FROM microsoft/ansible:latest

ARG ssh_prv_key
ARG ssh_pub_key

# Add the keys and set permissions
RUN echo "$ssh_prv_key" > /root/.ssh/id_rsa && \
  echo "$ssh_pub_key" > /root/.ssh/id_rsa.pub && \
  chmod 600 /root/.ssh/id_rsa && \
  chmod 600 /root/.ssh/id_rsa.pub

ENV VSCODEEXT_USER_AGENT=vscoss.vscode-ansible-0.5.2
COPY / /bones

WORKDIR /bones
RUN chmod -v 700 $(pwd)
ENTRYPOINT ["ansible-playbook"]