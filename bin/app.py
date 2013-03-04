#! /usr/bin/env python

"""
Author: tekulvw

A paper route payment tracker
"""

import web.py

urls = (
    '/', 'Index',
    '/pay', 'Payment',
    '/check', 'Check'
)

app = web.application(urls, globals())
render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        return render.index()
        
class Payment(object):
    def GET(self):
        return render.pay()
        
    def POST(self):
        return render.pay_saved()
        
class Check(object):
    def GET(self):
        return render.check_select()
        
    def POST(self):
        return render.check_show()
        
if __name__ == "__main__":
    app.run()
