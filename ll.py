#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#Cuauhtemoc Herrera Muñoz
#Universidad de Guadalajara
#Compiladores

class ll:
	
	def __init__( self, tokens ):
		self.tokens = tokens
		self.inputStack = list( )
		self.outputStack =list( )
		self.error = False
		self.inputStack.append( token( '$', '$' ) )
		for i in reversed( tokens ):
			self.inputStack.append( i )
		self.table = {
			's1' : { 'ID' : '1', 'PRINT' : '1', '$' : 2 },
			's' : { 'ID' : '3', 'PRINT' : '4' }
		}
		
	def analyze( ):
		self.outputStack.append( '$' )
		self.outputStack.append( 'S1' )
		flag = 'Analizando'
		while( flag == 'Analizando' ):
			i1 = self.inputStack[ len( self.inputStack ) - 1 ]
			i2 = self.outputStack[ len( self.outputStack ) - 1 ]
			print( i1.getStr( ), i2 )
			flag = ''