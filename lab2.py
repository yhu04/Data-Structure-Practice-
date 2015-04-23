"""This module provides an implementation of the Bag ADT.

The ADT is implemented in class Bag.

Author: Yue Hu
"""

from array import Array

class Vector:
	def __init__ ( self, size ):
		""" Constructs an empty vector with an initial capacity of two elements.""" 
		size=2
		self._theVect = Array( size )
        self.length=0
	
	def __len__ ( self ):
		""" Returns the number of items in the vector."""
		return self.length 

	def __contains__ ( self, item ):
		""" Determines if an item is contained in the vector.""" 
		return item in self._theVect

	def __getitem__ ( self, ndx ):
		""" Get the item at the ndx position.""" 
		assert ndx>0 and ndx<self.length, "Out of range"
		return self._theVect[ndx]

	def __setitem__ ( self, ndx, item ):
		""" Set the item at the ndx position.""" 
		assert ndx>=0 and ndx<self.length, "Out of range"
		self._theVect[ndx] = item 

	def append ( self, item ):
		""" Add the given item to the end of the list."""
		theVector=Array(len(self._theVect))
        for i in range(len(thenewVector)):
            theVector[i]=self._theVect[i]
        self._theVect=Array(len(self._theVect)＊2)
        for i in range(len(self._theVect)-1):
            self._theVect[i]=theVector[i]
        self._theVect[len(theVector)]=item 


    def insert ( self, ndx, item ):
    	"""Insert an item in the vector based on the given index."""
    	assert ndx>0 and ndx<=self.length, "Out of Scope"

    def extend ( self, otherVector ):
    	thecmbVector 
    		
    			



    def remove ( self, ndx):
    	"""Remove an index of the item in the vector."""
    	assert ndx>=0 and ndx<self.length, "Out of Scope"
    	for i in range(ndx-1,len(self._theVect)):
    		self._theVect[i]=self._theVect[i+1]

    def indexof ( self, item ):
    	"""Returns an index of the item in the vector."""
    	assert item in self._theVect, "The item is not in the vector."
    	for index in range(len(self._theVect)):
    		if self._theVect[index]=item:
    			return index 


	def subVector ( self, from, to ):
		return self._theVect[from,to+1]

	def __iter__ (self):
	    """Returns an iterator for traversing the list of items in the vector."""
	    return _VectorIterator(self._theItems)

    class _VectorIterator:
    	def __init__( self, theArray ):
    		self._vectorItems = theArray
    		self._curItem = 0

    	def __iter__ (self):
    		return self 

    	def __next__ (self):
    		if self.curItem < len(self._vectorItems):
    			item = self._vectorItems[self._curItem]
    			self.curItem += 1
    			return item 
    		else:
    			raise StopIteration 
