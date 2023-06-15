import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Affichage:
    def __init__(self, data):
        self.data = data
        self.x_cartesian = [colonne[7] for colonne in self.data]
        self.y_cartesian = [colonne[8] for colonne in self.data]
        self.z_cartesian = [colonne[9] for colonne in self.data]

    def plot_trajectory(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(self.x_cartesian, self.y_cartesian, self.z_cartesian)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

    def affichage_plan_de_vol(self):
        pass

    def affichage_physique(self):
        pass

