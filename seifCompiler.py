#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#Cuauhtemoc Herrera Muñoz
#Universidad de Guadalajara
#Compiladores

from lexicAn import *
from fileMan import *


class seifCompiler:

	def __init__( self ):
		self.data = ''
		self.lAnalizer = lexicAn( )
		self.result = ''
		self.dataMan = fileMan( )
			
	
	def analize( self ):
		self.lAnalizer.tokenizer( self.data )
		temp = self.lAnalizer.identifier( )
		if( self.lAnalizer.errorRaised( ) ):
			result = '0'
			return -1
		else:
			 
			self.dataMan.writeTxtFile( 'salida.txt', str( temp ) )

	def run( self ):
		self.data = self.dataMan.loadTxtFile( 'entrada.txt' )
		self.analize( )
		
		
app = seifCompiler( )
app.run( )

