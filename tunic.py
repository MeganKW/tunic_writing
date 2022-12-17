import matplotlib.pyplot as plt
import numpy as np
from matplotlib import collections  as mc

def hex_grid():
    """_summary_
    """
    pi = np.pi
    points = [np.sin(pi/3),np.cos(pi/3)]
    return points

def get_lines():
    outer_hex_code = [0,0,0,0,0,0]
    
    lines = [[(0, 1), (1, 1)], [(2, 3), (3, 3)], [(1, 2), (1, 3)]]
    return lines
        
def translate_lines(lines: list[list[tuple[int,int]]], t_x: float, t_y: float):
    """
    """


def get_line_collection(lines, color = 'black', linewidth = 2):
    """
    """
    lc = mc.LineCollection(lines, color, linewidth)
    return lc

def plot_lines(lines, ax = None, color = 'black', linewidth = 2):
    """_summary_

    Args:
        lines (_type_): _description_
        color (_type_): _description_
        linewidth (_type_): _description_
    """
    lc = get_line_collection(lines, color, linewidth)
    
    ax = ax or plt.gca()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    ax.axis('off')
    return ax