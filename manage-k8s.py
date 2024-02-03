'''
Script aim to manage deployment of kubrnetes cluster
to nodes using kubespray.
This is initially developed to be used to vms created on vsphere
'''

'''
Steps:
======
- run terraform to create infrastructure
- install haproxy on haproxy server
- configure haproxy with server and domain name
- create ansible inventory file
- create cluster/deployment variables
- run cluster creation using docker container
- get cluster credentials and put them in an accessible location
- helm install ingress addons
'''




