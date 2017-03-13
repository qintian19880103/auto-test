#coding:utf-8

from handlers.index import *


urls = [
(r'/', Main),
(r'^/main\.action$' , Main),
(r'^/nmap!result\.action$', Nmap_Result),
(r'^/dirb!result\.action$',Dirb_Result),
(r'^/subdomainsbrute!result\.action$',SubDomainsBrute),
]
