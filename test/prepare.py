import json
from decorator import decorator
from fabric.api import env, execute, parallel
from subprocess import call

env.key_filename = '/root/.ssh/couchbase-us-east-1.pem'

with open("details.txt", 'r') as f:
    datastore = json.load(f)

reservations = datastore["Reservations"]

ip_list_public = []
ip_list_private = []
for reservation in reservations:
    instances = reservation["Instances"]
    for instance in instances:
        tags = instance["Tags"]
        for tag in tags:
            if tag["Key"] == "aws:cloudformation:stack-name" and tag["Value"] == "a-test":
                ip_list_public.append(instance["PublicIpAddress"])
                ip_list_private.append(instance["PrivateIpAddress"])

print ip_list_public
print ip_list_private

@decorator
def all_servers(task, *args, **kwargs):

    hosts = ip_list_public

    return execute(parallel(task), *args, hosts=hosts, **kwargs)

@all_servers
def make_ssh_ready():
    call("echo -e 'couchbase\ncouchbase' | sudo passwd")
    call("sudo sed -i '/#PermitRootLogin yes/c\PermitRootLogin yes' /etc/ssh/sshd_config")
    call("sudo sed -i '/PermitRootLogin forced-commands-only/c\#PermitRootLogin forced-commands-only' /etc/ssh/sshd_config")
    call("sudo sed -i '/PasswordAuthentication no/c\PasswordAuthentication yes' /etc/ssh/sshd_config")
    call("sudo service sshd restart")

make_ssh_ready()
