import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class TrajectoryDisplay:
    def __init__(self, rocket):
        self.rocket = rocket

    def plot_trajectory(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(self.rocket.x_cartesian, self.rocket.y_cartesian, self.rocket.z_cartesian)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

    def affichage_plan_de_vol(self):
        pass

    def affichage_physique(self):
        pass

