
import matplotlib.pyplot as plt

class Graph:
    
    def __init__(self, x_data, y_data, title=None, xlabel=None, ylabel=None):
        self.x_data = x_data
        self.y_data = y_data
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        
    def line_plot(self):
        plt.plot(self.x_data, self.y_data)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()
        
    def scatter_plot(self):
        plt.scatter(self.x_data, self.y_data)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()
        
    def bar_plot(self):
        plt.bar(self.x_data, self.y_data)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

# Example usage
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 6, 8, 10]

graph = Graph(x_data, y_data, title="My Graph", xlabel="X Values", ylabel="Y Values")

graph.line_plot()
graph.scatter_plot()
graph.bar_plot()
