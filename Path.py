class Path(object):
    """
    Class of Paths
    """

    def __init__(self):
        """
        Constructs a map of the island with Paths 
        
        Ensures:
        Paths such that [] == self.getStations() and {} == self.getLinks() 
        """
        self._stations = []
        self._links = {}

        
    def addStation(self, station):
        """
        Adds a Station
        
        Requires:
        station is a Station
        Ensures:
        getStations() == getStations()@pre.append(station)
        getLinks[station] == [] 
        """
        if station in self._stations:
            raise ValueError('Duplicate station')
        else:
            self._stations.append(station)
            self._links[station] = []

            
    def addLink(self, link):
        src = link.getSource()
        dest = link.getDestination()
        if not(src in self._stations and dest in self._stations):
            raise ValueError('Station not in map')
        self._links[src].append(dest)

        
    def source(self, station):
        return self._links[station]

    
    def hasStation(self, station):
        return station in self._stations

    
    def __str__(self):
        result = ''
        for src in self._stations:
            for dest in self._links[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'



