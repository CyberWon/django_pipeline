import logging
from pipeline.core.flow.activity import Service
from pipeline.component_framework.component import Component


class FabricService(Service):
    def execute(self, data, parent_data):
        print("fabric")
        return True

    def outputs_format(self):
        return []


class FabricComponent(Component):
    name = "远程执行命令(SSH)-fabric"
    code = 'ssh_fabric'
    form="/static/components/atoms/ssh/fabric.js"
    bound_service = FabricService


class AnsibleService(Service):
    def execute(self, data, parent_data):
        print("ansible")
        return True

    def outputs_format(self):
        return []


class AnsibleComponent(Component):
    name = "远程执行命令(SSH)-ansible"
    code = 'ssh_ansible'
    form = "/static/components/atoms/ssh/ansible.js"
    bound_service = AnsibleService


class AnsiblePlaybookService(Service):
    def execute(self, data, parent_data):
        print("ansible-playbook")
        return True

    def outputs_format(self):
        return []


class AnsibleComponent(Component):
    name = "远程执行命令(SSH)-ansible_playbook"
    code = 'ssh_ansible_playbook'
    form = "/static/components/atoms/ssh/ansible_playbook.js"
    bound_service = AnsiblePlaybookService
