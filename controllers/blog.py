# -*- coding: utf-8 -*-
# 嘗試如
def index(): return dict(message="hello from blog.py")

def post():
    form = SQLFORM(db.blog).process()
    return locals()

def view():
    rows = db(db.blog).select(orderby==~db.blog.id)
    return locals()
