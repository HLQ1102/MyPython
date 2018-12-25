#!/usr/local/bin/python3

import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
passwords = dict()
inventory = InventoryManager(loader=loader, sources=['myansi/hosts'])
variable_manager = VariableManager(loader=loader, inventory=inventory)

play_source = dict(
        name="My Ansible Play Test",   # Play的名字
        hosts='webservers',  # 在哪些主机上执行任务
        gather_facts='no',   # 不收集主机信息
        tasks=[   # 要执行的命令
            dict(action=dict(module='shell', args='mkdir /tmp/abcd'), register='shell_out'),
         ]
    )

play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
tqm = None

try:
    tqm = TaskQueueManager(
              inventory=inventory,
              variable_manager=variable_manager,
              loader=loader,
              options=options,
              passwords=passwords,
          )
    result = tqm.run(play) # most interesting data for a play is actually sent to the callback's methods
finally:
    if tqm is not None:
        tqm.cleanup()
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
