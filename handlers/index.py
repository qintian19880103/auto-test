#coding:utf-8

import tornado.web
from model.entity import Entity

class Main(tornado.web.RequestHandler):
  def get(self):
    templates = 'list.html'
    self.render('main.html',templates = templates)

class Nmap_Result(tornado.web.RequestHandler):
  def get(self):
    templates = 'nmap_result.html'
    self.render('main.html',templates = templates)

class Dirb_Result(tornado.web.RequestHandler):
  def get(self):
    templates = 'dirb_result.html'
    self.render('main.html',templates = templates)

class SubDomainsBrute(tornado.web.RequestHandler):
  def get(self):
    templates = 'subdomainsbrute_result.html'
    self.render('main.html',templates = templates)
		