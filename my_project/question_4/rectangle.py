# class Rectangle:
#     def __init__(self, length: int, width: int):
#         self.length = length
#         self.width = width
    
#     def __iter__(self):
#         # Generator function for iteration
#         yield {'length': self.length}
#         yield {'width': self.width}


class Rectangle:
    def __init__(self, *rectangles):
        """
        Initializes with a variable number of (length, width) tuples.
        """
        self.rectangles = rectangles
    
    def __iter__(self):
        """
        Allows iteration over the rectangle instances.
        """
        for length, width in self.rectangles:
            yield {'length': length}
            yield {'width': width}
