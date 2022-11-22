__doc__ = '''
    *chain.py*
    Module that integrate a representation of a chained list in Python,
    which is a infinite looping list.
    
    Example:
        li = Chain([1, 2, 3])   # Initialize
        print(li[1000])         # get element
        print(li[0:1000:4])     # slices also work
'''

from typing import Union, Any

class Chain(list):
    '''
    Represents a chained list.
    '''
    
    def __getitem__(self, index: Union[slice, int]) -> Any:
        
        if isinstance(index, slice):
            
            res = []
            i = index.start
            step = index.step or 1
            stop = index.stop if index.stop >= 0 else self.__len__()
            
            while i < stop:
                res.append(self.__getitem__(i))
                i += step
            
            return res
        
        return super().__getitem__(index % self.__len__())

# EOF