#coding:utf-8

import tornado.web
import subprocess
from model.db import db


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

class Add_Task(tornado.web.RequestHandler):
  def post(self):
    tool = self.get_argument("tool")
    parameter = self.get_argument("parameter")
    name = self.get_argument("name")
    respath = self.get_argument("name")
    result = subprocess.Popen("%s %s" %(tool,parameter))
    '''
        create table if  not exists  project(
        id             int       primary key    not null,
        name           char(80)  not null,
        taskid         int       not null,
        respath        char(50)  not null,
        status         int       not null 
        );
    '''
    db.insert({"name":name,"taskid":result.pid,"respath":respath,"status":0})
    return 



