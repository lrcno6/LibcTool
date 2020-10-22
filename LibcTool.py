#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'A class to use LibcSearcher more conveniently'
__author__='lrcno6'
import LibcSearcher
class LibcTool(object):
	def __init__(self,func,addr):
		self.__searcher=LibcSearcher.LibcSearcher(func,addr)
		self.__first_func=func
		self.__addr=addr
	def add_condition(self,func,addr):
		self.__searcher.add_condition(func,addr)
	def dump(self,func):
		if self.__first_func is not None:
			self.__addr-=self.__searcher.dump(self.__first_func)
			self.__first_func=None
		return self.__addr+self.__searcher.dump(func)