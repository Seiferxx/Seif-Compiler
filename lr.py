#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#Cuauhtemoc Herrera Muñoz
#Universidad de Guadalajara
#Compiladores

from token import *
from tokenTypes import *

class lr:
	
	def __init__( self , tokens ):
		self.tokens = tokens
		self.inputStack = list( )
		self.outputStack =list( )
		self.actionStack = list( )
		self.error = False
		self.inputStack.append( token( '$', '$' ) )
		for i in reversed( tokens ):
			self.inputStack.append( i )
		self.table =  {
			'OPPLUS': { '0' : 'd-3', '2' : 'd-6', '3' : 'd-3', '4' : 'd-3', '5' : 'd-3', '6' : 'd-3', '7' : 'd-3', '8' : 'd-6', '9' : 'd-6', '11' : 'r-3', '12' : 'r-4', '13' : 'r-6', '14' : 'r-7'  },
			'OPTIMES' : { '2' : 'd-7', '8' : 'd-7',  '9' : 'd-7', '11' : 'd-7', '12' : 'r-4', '13' : 'r-6', '14' : 'r-7' },
			'LEFTPAR' : { '0' : 'd-4', '3' : 'd-4', '5' : 'd-4', '6' : 'd-4', '7' : 'd-4' },
			'RIGHTPAR' : { '8' : 'r-5', '9' : 'd-13', '11' : 'r-3', '12' : 'r-4', '13' : 'r-6', '14' : 'r-7' },
			'DELIM' : { '2' : 'd-5', '8' : 'r-5', '11' : 'r-3', '12' : 'r-4', '13' : 'r-6', '14' : 'r-7' },
			'$' : { '0' : 'r-2' , '1' : 'ok' , '5' : 'r-2', '10' : 'r-1' },
			'ID' : { '0' : 'd-14', '3' : 'd-14', '4' : 'd-14', '5' : 'd-14',  '6' : 'd-14', '7' : 'd-14' },
			'S' : { '0' : '1', '5' : '10' },
			'E' : { '0' : '2', '3' : '8', '4' : '9', '5' : '2', '6' : '11', '7' : '12' }
		}
	
	
	def analyze( self ):
		self.actions = "";
		self.outputStack.append( '$' )
		self.outputStack.append( '0' )
		flag = 'Analizando'
		while( flag == 'Analizando' ):
			i1 = self.inputStack[ len( self.inputStack ) - 1 ]
			i2 = self.outputStack[ len( self.outputStack ) - 1 ]
			print( i1.getStr( ), i2 )
			try:
				val = self.table[ i1.getType( ) ][ i2 ]
				print( val )
				if( len( val ) < 3 ):
					if( val == 'ok' ):
						flag = 'Terminado'
						self.actions = self.actions + 'Aceptacion' + " "
				else:
					t = val.split( "-" )[ 0 ]
					v = val.split( "-" )[ 1 ]
					print( t, v )
					self.actions = self.actions + t + v + " "
					if( t == 'd' ):
						self.inputStack.pop( )
						self.outputStack.append( i1.getType( ) )
						self.outputStack.append( v )
						print( self.outputStack )
					else:
						if( v == '7' ):
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.append( 'E' )
							print( self.outputStack )
							n = self.table[ 'E' ][ self.outputStack[ len( self.outputStack ) - 2 ] ]
							self.outputStack.append( n );
							self.actions = self.actions + n + " "
							print( self.outputStack )
						elif( v == '3' ):
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.append( 'E' )
							print( self.outputStack )
							n = self.table[ 'E' ][ self.outputStack[ len( self.outputStack ) - 2 ] ]
							self.outputStack.append( n );
							self.actions = self.actions + n + " "
							print( self.outputStack )
						elif( v == '2' ):
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.append( 'S' )
							print( self.outputStack )
							n = self.table[ 'S' ][ self.outputStack[ len( self.outputStack ) - 2 ] ]
							self.outputStack.append( n );
							self.actions = self.actions + n + " "
							print( self.outputStack )
						elif( v == '1' ):
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.append( 'S' )
							print( self.outputStack )
							n = self.table[ 'S' ][ self.outputStack[ len( self.outputStack ) - 2 ] ]
							self.outputStack.append( n );
							self.actions = self.actions + n + " "
							print( self.outputStack )
						elif( v == '4' ):
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.append( 'E' )
							print( self.outputStack )
							n = self.table[ 'E' ][ self.outputStack[ len( self.outputStack ) - 2 ] ]
							self.outputStack.append( n );
							print( self.outputStack )
						elif( v == '5' ):
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.append( 'E' )
							print( self.outputStack )
							n = self.table[ 'E' ][ self.outputStack[ len( self.outputStack ) - 2 ] ]
							self.outputStack.append( n );
							self.actions = self.actions + n + " "
							print( self.outputStack )
						elif( v == '6' ):
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.pop( )
							self.outputStack.append( 'E' )
							print( self.outputStack )
							n = self.table[ 'E' ][ self.outputStack[ len( self.outputStack ) - 2 ] ]
							self.outputStack.append( n );
							self.actions = self.actions + n + " "
							print( self.outputStack )
			except( KeyError ):
				flag = 'Error'
				self.error = True
				self.actions = self.actions + 'Error' + " "
		print( self.actions )
		return self.actions
		
	def errorRaised( self ):
		return self.error
		
	def getActions( self ):
		return self.actions