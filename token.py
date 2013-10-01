#!/usr/bin/env python3
#coding: utf-8
#Cuauhtemoc Herrera Muñoz
#Universidad de Guadalajara
#Compiladores

class token:
	
	def __init__( self, _type, _str  ):
		self._type = _type
		self._str = _str
		
	def getType( self ):
		return self._type
		
	def getStr( self ):
		return self._type
