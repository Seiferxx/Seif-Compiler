

class lr:
	
	def __init__( self , tokens ):
		self.tokens = tokens
		self.inputStack = list( )
		self.outputStack =list( )
		self.actionStack = list( )
		for i in reversed( tokens ):
			self.inputStack.append( i )
		self.table =  {
		'OPPLUS': { 0 : 'd3', 2 : 'd6', 3 : 'd3', 4 : 'd3', 5 : 'd3', 6 : 'd3', 7 : 'd6', 8 : 'd6', 9 : 'd6', 11 : 'r3', 12 : 'r4', 13 : 'r6', 14 : 'r7'  },
		'OPTIMES' : { 2 : 'd7', 8 : 'd7',  9 : 'd7', 11 : 'd7', 12 : 'r4', 13 : 'r6', 14 : 'r7' },
		'LEFTPAR' : { 0 : 'd4', 3 : 'd4', 5 : 'd4', 6 : 'd4', 7 : 'd4' },
		'RIGHTPAR' : { 8 : 'r5', 9 : 'd13', 11 : 'r3', 12 : 'r4', 13 : 'r6', 14 : 'r7' },
		'DELIM' : { 2 : 'd5', 8 : 'r5', 11 : 'r3', 12 : 'r4', 13 : 'r6', 14 : 'r7' },
		'$' : {},
		'ID' : {},
		'S' : {},
		'E' : {}
		}
	
app = lr( [1,2] )