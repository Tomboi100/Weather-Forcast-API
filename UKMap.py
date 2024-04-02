"""A class that plots longitude/latitude points on a UK map background.
No projection is applied so some warping will occur. The Basemap toolkit
for matplotlib handles maps/projections better but is not installed by
default on the university machines. This is a simple alternative."""

import matplotlib.pyplot as plt

class UKMap:
    def __init__(self):
        m = plt.imread("Gb4dot_merged_mapcolors.png")
        plt.imshow(m, extent=[-9,2,50,59])
        plt.axis([-9,2,50,59])
        
    def plot(self, x, y, marker='.', markersize='2', color='blue'):
        """Plot a single point on the map.
        Note: Parameter x should be longitude, and y should be latitude"""
        plt.plot(x, y, marker=marker, markersize=markersize, color=color)

    def show(self):
        plt.show()

    def savefig(self,*args,**kwargs):
        """Just call matplotlib's savefig method directly with all the arguments"""
        plt.savefig(*args, **kwargs)


if __name__ == "__main__":
    m = UKMap()
    #53.99,-1.04
    m.plot(-1.04, 53.99, marker='o')
    m.plot(-4.064598, 52.41616, marker='o')
    m.show()
