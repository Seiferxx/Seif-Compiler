from Lexican import *


class SeifCompiler:

	def __init__( self ):
		self.data = ''
	
	def LoadFile( self, filename ):
		"""Funcion para cargar el archivo origen y leer su contenido"""
		try:
			f_buffer = open( filename, 'w' )
			self.data = f_buffer.read( )
		except IOError:
			print( 'Error al intentar cargar el archivo' )
	
	def Analize( self ):
		pass
