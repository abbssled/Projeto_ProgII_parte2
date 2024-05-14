class Link(object):
    """
    Class of Links
    """
    
    def __init__(self, src, dest):
        """
        Constructs an Edge
        
        Requires:
        src and dst Stations
        Ensures:
        Link such that src == self.getSource() and dest == self.getDestination() 
        """
        self._src = src
        self._dest = dest

        
    def getSource(self):
        """
        Gets the source Station
        """
        return self._src

    
    def getDestination(self):
        """
        Gets the destination Station
        """
        return self._dest


    def __str__(self):
        """
        String representation
        """
        return self._src.getName() + '->' + self._dest.getName()