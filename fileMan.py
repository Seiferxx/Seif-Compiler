#!/usr/bin/env python3
#coding: utf-8
#Cuauhtemoc Herrera Muñoz
#Universidad de Guadalajara
#Compiladores


class fileMan:

	
	def __init__( self ):
		self.fBuffer = None
		
	def createTxtFile( self, filename ):
		try:
			self.fBuffer = open( filename, 'w' )
			self.fBuffer.close( )
		except IOError:
			print( 'Error: ' )
			
	def createBinFile( self, filename ):
		try:
			self.fBuffer = open( filename, 'wb' )
			self.fBuffer.close( )
		except IOError:
			print( 'Error: ' )
			
	def loadTxtFile( self, filename ):
		data = ''
		try:
			self.fBuffer = open( filename, 'r' )
			data = self.fBuffer.read( )
			self.fBuffer.close( )
			return data
		except IOError:
			print( 'Error: ' )
			
	def loadBinFile( self, filename ):
		#Not implemented yet
		pass
		
	def writeTxtFile( self, filename, data ):
		try:
			self.fBuffer = open( filename, 'w' )
			self.fBuffer.write( data )
			self.fBuffer.close( )
		except IOError:
			print( 'Error: ' )
			
	def writeBinFile( self, filename, data ):
		#Not implemented yet
		pass
		
	def appendTxtFile( self, filename, data ):
		try:
			self.fBuffer = open( filename, 'a' )
			self.fBuffer.write( data )
			self.fBuffer.close( )
		except IOError:
			print( 'Error: ' )
			
	def appendBinFile( self, filename, data ):
		#Not implemented yet
		pass
