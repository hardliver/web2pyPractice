# -*- coding: utf-8 -*-
# 嘗試如
def request_object():
    app = request.application
    cntr = request.controller
    fx = request.function
    ext = request.extension
    folder = request.folder
    now = request.now
    client = request.client
    isSecure = request.is_https
    return locals()

def request_vars():
    num1 = 0
    num2 = 0
    total = 0
    if request.post_vars:
        num1 = float(request.post_vars.num1)
        num2 = float(request.post_vars.num2)
        total = num1 + num2
    return locals()

def request_args():
    arg1 = float(request.args(0))
    arg2 = float(request.args(1))
    total = arg1 + arg2
    return locals()

def helloworld():
    msg = "Hello from the Controller!"
    return locals()

def index():
    return dict(message="hello from basics.py")
