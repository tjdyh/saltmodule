# -*- coding: utf-8 -*-
'''
The top nth processes which take up CPU and memory space usage are available through this module, additionaly;
the module can get the system load information.
'''

#Import python libs
import os
# Import salt libs
import salt.utils
from pprint import pprint
def cpu(n):
    '''
    Return the top nth processes which take up the momory usage for this minion
    CLI Example:
    salt '*' prank.cpu <n>
    '''
    cmd = "ps -axu|sort -k3 -nr|head -n%s" % str(n)
    output = __salt__['cmd.run_all'](cmd)
    pprint(stdout)
    res = []
    for line in output.splitlines():
        res.append(line)
    return res

def mem(n):
    '''
    Return the top nth processes which take up the CPU usage for this minion
    CLI Example:
    salt '*' prank.mem <n>
    '''
    cmd = "ps axu|sort -k4 -nr|head -n %s" % str(n)
    output = __salt__['cmd.run_stdout'](cmd)
    res = []
    for line in output.splitlines():
        res.append(line)
    return res

def load():
    '''
    Retturn the load averages for this minion
    CLI Example:
    .. code-block:: bash
    salt '*' prank.loadavg
    '''
    load_avg = os.getloadavg()
    return {'1-min': load_avg[0],
           '5-min': load_avg[1],
           '15-min': load_avg[2]}

def test():
    '''
    做个测试
    :return:
    '''
    cmd = "free -m"
    out_test = __salt__['cmd.run_stdout'](cmd)
    return out_test
    # return "this is test"