import timeit

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def check():
    g_algo = GraphAlgo()
    file = "../data/G_10_80_1.json"
    print("file_name is: ", file)
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    algo(g_algo)

    g_algo = GraphAlgo()
    file = "../data/G_100_800_1.json"
    print("file_name is: ", file)
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    algo(g_algo)

    g_algo = GraphAlgo()
    file = "../data/G_1000_8000_1.json"
    print("file_name is: ", file)
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    algo(g_algo)

    g_algo = GraphAlgo()
    file = "../data/G_10000_80000_1.json"
    print("file_name is: ", file)
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    algo(g_algo)

    g_algo = GraphAlgo()
    file = "../data/G_20000_160000_1.json"
    print("file_name is: ", file)
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    algo(g_algo)

    g_algo = GraphAlgo()
    file = "../data/G_30000_240000_1.json"
    print("file_name is: ", file)
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    algo(g_algo)


def algo(g_algo):
    start = timeit.default_timer()
    g_algo.shortest_path(1, 7)
    stop = timeit.default_timer()
    print('Time_short_pass: ', stop - start)

    start = timeit.default_timer()
    g_algo.connected_components()
    stop = timeit.default_timer()
    print('Time_connected_components: ', stop - start)

    start = timeit.default_timer()
    g_algo.connected_component(0)
    stop = timeit.default_timer()
    print('Time_connected_component: ', stop - start)


if __name__ == '__main__':
    check()
