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
    name = "fabric"
    code = 'fabric'
    bound_service = FabricService


class AnsibleService(Service):
    def execute(self, data, parent_data):
        print("ansible")
        return True

    def outputs_format(self):
        return []


class AnsibleComponent(Component):
    name = "ansible"
    code = 'ansible'
    bound_service = AnsibleService


class AnsiblePlaybookService(Service):
    def execute(self, data, parent_data):
        print("ansible-playbook")
        return True

    def outputs_format(self):
        return []


class AnsibleComponent(Component):
    name = "ansible_playbook"
    code = 'ansible_playbook'
    bound_service = AnsiblePlaybookService
