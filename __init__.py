__version__ = '1.0.0'


from pysymanalysis.sym import Symmetry


class SymAnalysisTask():

    def __init__(self, name, symmetry: Symmetry, dangling_bonds, syop_dangling_bonds):
        self.name = name
        self.symmetry = symmetry
        self.dangling_bonds = dangling_bonds
        self.syop_dangling_bonds = syop_dangling_bonds

