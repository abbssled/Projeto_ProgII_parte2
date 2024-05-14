from Station import Station
from Link import Link
from Path import Path

class Options(Path):
    """
    asfafdfdafs
    """

    def addLink(self, link):
        Path.addLink(self, link)
        rev = Link(link.getDestination(), link.getSource())
        Path.addLink(self, rev)