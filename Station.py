class Station(object):
    """
    Class of Stations
    """

    def __init__(self, id, name):
        """
        Constructs a Station
        
        Requires:
        id and name is a string and connection is a list
        Ensures:
        station such that id == self.getId(), name == self.getName()
        """
        self._id = id
        self._name = name


    def getId(self):
        """
        Gets the id
        """
        return self._id
    

    def getName(self):
        """
        Gets the name
        """
        return self._name


    def __str__(self):
        """
        String representation
        """
        return self._name

