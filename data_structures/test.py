# Author: Dahir Muhammad Dahir
# Date: 19-June-2019 8:29 PM
# About: this file is used to test the implementation of
# the various data structures found in this module


from bidirectional_graph import BiGraph


def main():
    graph1 = BiGraph(5)
    graph2 = BiGraph(3)
    graph1.add_edge((0, 1))
    graph1.add_edge((0, 4))
    graph1.add_edge((1, 2))
    graph1.add_edge((1, 3))
    graph1.add_edge((1, 4))
    graph1.add_edge((2, 3))
    graph1.add_edge((3, 4))

    graph2.add_edge((0, 1))
    graph2.add_edge((1, 2))
    graph2.add_edge((2, 0))

    graph1.print_graph()
    graph2.print_graph()


if __name__ == "__main__":
    main()
