from __future__ import absolute_import

import logging

from library.connecter.ansible.v2_3.adhoc import adhoc
from library.connecter.ansible.v2_3.playbook import playbook 
from devops.celery import app
from celery.signals import worker_process_init
from multiprocessing import current_process
logger = logging.getLogger("devops")

@worker_process_init.connect
def fix_multiprocessing(**kwargs):
    try:
        current_process()._config
    except AttributeError:
        current_process()._config = {'semprefix': '/mp'}

@app.task
def ansible_send_adhoc(name, username, option_dict, describe, inve_protect_content):
    ansible_api = adhoc('adhoc', name, username, option_dict, describe)
    result = ansible_api.run(inve_protect_content, 'all')
    logger.warn('为用户' + username + '发送一个名为' + name + '的ansible临时任务给后台执行')
    return result


@app.task
def ansible_send_playbook(name, username, option_dict, describe, inve_protect_content, main_file, vault_password):
    ansible_api = playbook('playbook', name, username, option_dict, describe)
    result = ansible_api.run(main_file, vault_password, inve_protect_content)
    logger.warn('为用户' + username + '发送一个名为' + name + '的ansible playbook任务给后台执行')
    return result
