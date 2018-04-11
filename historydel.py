# -*- coding: utf-8 -*-
import os

def hisdel():
    '''
    delete history commond;
    :return:
    '''
    os.system(':>/root/.bash_history')
    return "history has deleted!"

if __name__ == '__main__':
    hisdel()
