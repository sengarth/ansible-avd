from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = {}
        result["ansible_facts"] = self._task.args
        return result
