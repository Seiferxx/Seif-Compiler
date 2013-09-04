#-*- coding: utf-8 -*-
#Cuauhtemoc Herrera Muñoz
#Universidad de Guadalajara
#Compiladores

from re import split
from re import match

class LexicAn:
	"""Clase que realiza el analisis lexicografico de un archivo"""
	
	def __init__( self ):
		"""Constructor de la clase"""
		self.tokens = list( )
	
	def Tokenizer( self, text ):
		"""Tokenizer que devuelve una lista con los tokens que resultan de
		   dividir el texto"""
		lines = split( '\n', text )
		self.tokens = list( )
		for i in lines:
			for j in split( '(\+|\-|\*|/|\}|\{|\]|\[|\>|\<|\!\=|\=\=|\=|\!)', i ):
				j = j.strip( ' ' ) 
				if j != '':
					self.tokens.append( j )
		print self.tokens
		return self.tokens 
	
	def Identifier( self ):
		s = ''
		for i in self.tokens:
			if i == '+' or i == '-':
				s = s + i + ' : Operador\n'
			else:
				state = 0
				for j in i:
					if state == 0:
						if match( '[a-zA-Z_]', j ):
							state = 1
						elif match( '[0-9]', j ):
							state = 2
						else:
							state = -1
					elif state == 1:
						if match( '[a-zA-Z0-9_]', j ):
							state = 1
						else:
							state = -1
					elif state == 2:
						if match( '[0-9]', j ):
							state = 2
						elif j == '.':
							state = 3
						else:
							state = -1
					elif state == 3:
						if match( '[0-9]', j ):
							state = 3
						else:
							state = -1
					else:
						state = -1
				if state == 1:
					s = s + i + ' : Identificador\n'
				elif state == 2:
					s = s + i + ' : Numero Entero\n'
				elif state == 3:
					s = s + i + ' : Numero Real\n'
				else:
					s = s + i + ' : Error\n'
		print( s )

app = LexicAn( )
app.Tokenizer( "a+b\na-b\na*b\na/b\na>b\na<b\na!=b\na==b\na=b\n{a}[b]" )
