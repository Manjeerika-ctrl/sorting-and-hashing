class HashTable:
	def	__init__(self,	size):
		self.size	=	size
		self.table	=	[]
		for	i	in	range(size):
			self.table.append([])
	def	hash_function(self,	key):
	    return	key	%	self.size
def	insert(self,	key):
	index	=	self.hash_function(key)
	self.table[index].append(key)
def	search(self,	key):
	index	=	self.hash_function(key)
	if	key	in	self.table[index]:
		return	True
	return	False
def	display(self):
	for	i	in	range(self.size):
		print(i,	":",	self.table[i])
keys	=	[50,	21,	58,	17,	15,	49]
for	k	in	keys:
	ht.insert(k)