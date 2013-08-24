from re import split

class LexicAn:
	"""Clase que realiza el analisis lexicografico de un archivo"""
	
	def __init__( self ):
		pass
	
	def Tokenizer( self, text ):
		lines = split( '\n', text )
		print( lines )
		tokens = list( )
		for i in lines:
			for j in split( '(\+|\-)', i ):
				j = j.strip( '\s' ) 
				if j != '':
					tokens.append( j ) 
		print( tokens )
	
	def Identifier( self, tokens ):
		pass


algo = LexicAn( )
algo.Tokenizer( '++2x10\n4 + 3\nalfa - beta' )
