#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#Cuauhtemoc Herrera Muñoz
#Universidad de Guadalajara
#Compiladores

from lexicAn import *
from fileMan import *
from lr import *


class seifCompiler:

	def __init__( self ):
		self.data = ''
		self.lAnalizer = lexicAn( )
		self.result = ''
		self.dataMan = fileMan( )
			
	
	def analyze( self ):
		self.lAnalizer.tokenize( self.data )
		self.lAnalizer.identify( )
		if( self.lAnalizer.errorRaised( ) ):
			self.dataMan.writeTxtFile( 'salida.txt', '0' )
			self.dataMan.writeTxtFile( 'acciones.txt', 'Error Lexico' )
		else:
			self.syntAnalizer = lr( self.lAnalizer.getATokens( ) )
			self.syntAnalizer.analyze( )
			if( self.syntAnalizer.errorRaised( ) ):
				self.dataMan.writeTxtFile( 'salida.txt', '0' )
			else:
				self.dataMan.writeTxtFile( 'salida.txt', '1' )
			self.dataMan.writeTxtFile( 'acciones.txt', self.syntAnalizer.getActions( ) )
		

	def run( self ):
		self.data = self.dataMan.loadTxtFile( 'entrada.txt' )
		self.analyze( )
		
		
app = seifCompiler( )
app.run( )

