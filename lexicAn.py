#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#Cuauhtemoc Herrera Muñoz
#Universidad de Guadalajara
#Compiladores

from re import split
from re import match
from tokenTypes import *
from token import *

class lexicAn:
	"""Clase que realiza el analisis lexicografico"""
	
	def __init__( self ):
		"""Constructor de la clase"""
		self.tokens = list( )
		self.aTokens = list( )
		self.eFlag = False
	
	def tokenize( self, text ):
		"""Devuelve una lista con los tokens que resultan de
		   dividir el texto"""
		lines = split( '\n', text )
		self.tokens = list( )
		for i in lines:
			i = i.replace( '“', '\"' )
			i = i.replace( '”', '\"' )
			for j in split( '(\;|\,|\+|\-|\*|/|\}|\{|\)|\(|\<\=|\>\=|\>|\<|\!\=|\=\=|\=|\!|\&\&|\|\|)', i ):
				j = j.strip( ' ' )
				if ' ' in j:
					for k in split( ' ', j ):
						k = k.strip( ' ' )
						if k != '':
							self.tokens.append( k )
				else:
					if j != '':
						self.tokens.append( j )
		print( self.tokens )
		return self.tokens
	
	def identify( self ):
		s = ''
		totals = list( )
		ID = 0
		INT = 0
		FLOAT = 0
		CHAR = 0
		OPPLUS = 0
		OPTIMES = 0
		OPASSIGN = 0
		OPREL = 0
		OPLOG = 0
		LEFTPAR = 0
		RIGHTPAR = 0
		LEFTBRA = 0
		RIGHTBRA = 0
		DELIM = 0
		for i in self.tokens:
			if i == '+' or i == '-':
				s = s + i + ' : Operador Suma\n'
				self.aTokens.append( token( 'OPPLUS' ,i ) )
				OPPLUS = OPPLUS + 1
			elif i.upper == 'PRINT':
				s = s + i + ' : Identificador\n'
				self.aTokens.append( token( 'PRINT' ,i ) )
				ID = ID + 1
			elif i == '*' or i == '/':
				s = s + i + ' : Operador Multiplicacion\n'
				self.aTokens.append( token( 'OPTIMES' ,i ) )
				OPTIMES = OPTIMES + 1
			elif i == '>' or i == '<' or i == '<=' or i == '>=':
				s = s + i + ' : Operador Relacional\n'
				self.aTokens.append( token( 'OPREL' ,i ) )
				OPREL = OPREL + 1
			elif i == '!':
				s = s + i + ' : Operador Logico\n'
				self.aTokens.append( token( 'OPLOG'  ,i ) )
				OPLOG = OPLOG + 1
			elif i == '{' or i == '}':
				s = s + i + ' : Llave\n'
				if i == '{':
					LEFTBRA = LEFTBRA + 1
					self.aTokens.append( token( 'LEFTBRA' ,i ) )
				else:
					RIGHTBRA = RIGHTBRA + 1
					self.aTokens.append( token( 'RIGHTBRA' ,i ) )
			elif i == '(' or i == ')':
				s = s + i + ' : Parentesis\n'
				if i == '(':
					LEFTPAR = LEFTPAR + 1
					self.aTokens.append( token( 'LEFTPAR' ,i ) )
				else:
					RIGHTPAR = RIGHTPAR + 1
					self.aTokens.append( token( 'RIGHTPAR' ,i ) )
			elif i == '=':
				s = s + i + ' : Operador de Asignacion\n'
				self.aTokens.append( token( 'OPASSIGN' ,i ) )
				OPASSIGN = OPASSIGN + 1
			elif i == ';' or i == ',':
				s = s + i + ' : Delimitador\n'
				self.aTokens.append( token( 'DELIM' ,i ) )
				DELIM = DELIM + 1
			else:
				state = 0
				for j in i:
					if state == 0:
						if match( '[a-zA-Z_]', j ):
							state = 1
						elif match( '[0-9]', j ):
							state = 2
						elif j == '=':
							state = 4
						elif j == '!':
							state = 5
						elif j == '&':
							state = 6
						elif j == '|':
							state = 7
						elif j == '\"':
							state = 12
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
					elif state == 4:
						if j == '=':
							state = 8
						else:
							state = -1
					elif state == 5:
						if j == '=':
							state = 9
						else:
							state = -1
					elif state == 6:
						if j == '&':
							state = 10
						else:
							state = -1
					elif state == 7:
						if j == '|':
							state = 11
						else:
							state = -1
					elif state == 12:
						if j == '\"':
							state = 13
						elif match( '[a-zA-Z_]', j ):
							state = 12
						else:
							state = -1
					else:
						state = -1
				if state == 1:
					s = s + i + ' : Identificador\n'
					self.aTokens.append( token( 'ID' ,i ) )
					ID = ID + 1
				elif state == 2:
					s = s + i + ' : Numero Entero\n'
					self.aTokens.append( token( 'INT' ,i ) )
					INT = INT + 1
				elif state == 3:
					s = s + i + ' : Numero Real\n'
					self.aTokens.append( token( 'FLOAT' ,i ) )
					FLOAT = FLOAT + 1
				elif state == 8 or state == 9:
					s = s + i + ' : Operador Relacional\n'
					self.aTokens.append( token( 'OPREL' ,i ) )
					OPREL = OPREL + 1
				elif state == 10 or state == 11:
					s = s + i + ' : Operador Logico\n'
					self.aTokens.append( token( 'OPLOG',i ) )
					OPLOG = OPLOG + 1
				elif state == 13:
					s = s + i + ' : Cadena\n'
					self.aTokens.append( token( 'CHAR',i ) )
					CHAR = CHAR + 1
				else:
					s = s + i + ' : Error\n'
					self.eFlag = True
					return -1
		totals.append( ID )
		totals.append( INT )
		totals.append( FLOAT )
		totals.append( CHAR )
		totals.append( OPPLUS )
		totals.append( OPTIMES )
		totals.append( OPASSIGN )
		totals.append( OPREL )
		totals.append( OPLOG )
		totals.append( LEFTPAR )
		totals.append( RIGHTPAR )
		totals.append( LEFTBRA )
		totals.append( RIGHTBRA )
		totals.append( DELIM )
		#self.aTokens.append( token( 'EPSILON', '' ) )
		for i in self.aTokens:
			print( i.getType( ) )
		return totals
		
	def errorRaised( self ):
		if( self.eFlag ):
			return True
		return False
		
	def getATokens( self ):
		return self.aTokens
		
