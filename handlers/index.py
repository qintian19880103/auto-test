#coding:utf-8

import tornado.web
from model.entity import Entity

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    #entity = Entity.get('the5fire\'s blog')
    entity = 'aydon'
    #self.render('index.html', entity = 'Aydon')
    self.render('index.html', entity =  entity)
