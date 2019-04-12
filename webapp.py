#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web

from settings import render_plain

urls = (
	'/',	'index'
)

class index:
	def GET(self):
		return render_plain.index()

app = web.application(urls,globals())
wsgiapp = app.wsgifunc()
if __name__ == "__main__":
	app.run()
