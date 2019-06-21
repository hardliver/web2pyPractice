# -*- coding: utf-8 -*-
# 嘗試如
def helloworld():
    msg = "Hello from the Controller!"
    return locals()

def index():
    return dict(message="hello from basics.py")
