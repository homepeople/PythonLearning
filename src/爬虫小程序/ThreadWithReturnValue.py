# -*- coding: utf-8 -*-
import threading 

class ReturnValue(threading.Thread):
    def __init__(self, *init_args, **init_kwargs):
        threading.Thread.__init__(self, *init_args, **init_kwargs)
        self._return = None
        
    def run(self):
        print('loading')
        self._return = self._target(*self._args, **self._kwargs)
        
    def join(self):
        threading.Thread.join(self)
        return self._return