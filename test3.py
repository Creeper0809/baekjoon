import random
import time


def generate_random_graph(num_vertices, num_edges):
    graph = {vertex: [] for vertex in range(num_vertices)}

    # 간선 생성
    for _ in range(num_edges):
        # 두개의 랜덤한 노드 선택
        vertex1 = random.randint(0, num_vertices - 1)
        vertex2 = random.randint(0, num_vertices - 1)

        # 중복 제거
        if vertex1 != vertex2 and vertex2 not in graph[vertex1]:
            graph[vertex1].append(vertex2)
            graph[vertex2].append(vertex1)

    return graph


def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)


def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

num_vertices = 2000
num_edges = 3000

random_graph = generate_random_graph(num_vertices, num_edges)
for _ in range(5):
    start_time = time.time()
    dfs_recursive(random_graph,1)
    cac_time1 = time.time()-start_time
    print(f"재귀 dfs:{cac_time1}")
    start_time = time.time()
    dfs_stack(random_graph,1)
    cac_time2 = time.time() - start_time
    print(f"스택 dfs:{cac_time2}")
    print("재귀 승") if cac_time1<cac_time2 else print("스택 승")
    print("-"*30)
