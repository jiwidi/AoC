from collections import defaultdict, deque

def topological_sort(nodes, edges):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for n in nodes:
        in_degree[n] = 0
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    queue = deque([n for n in nodes if in_degree[n] == 0])
    ordering = []
    while queue:
        u = queue.popleft()
        ordering.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    if len(ordering) != len(nodes):
        # There is a cycle
        raise Exception("Cycle detected")
    return ordering

def part_one(rules, updates):
    r = 0
    for update in updates:
        update_dict = {v:i for i, v in enumerate(update)}
        update_correct = True
        for rule in rules:
            if rule[0] in update_dict and rule[1] in update_dict and update_dict[rule[0]] >= update_dict[rule[1]]:
                update_correct = False
                break
        if update_correct:
            r+=update[len(update)//2]
    return r


def part_two(rules, updates):
    r = 0
    for update in updates:
        update_dict = {v: i for i, v in enumerate(update)}
        update_correct = True
        for rule in rules:
            if (rule[0] in update_dict and rule[1] in update_dict and
                    update_dict[rule[0]] >= update_dict[rule[1]]):
                update_correct = False
                break
        if not update_correct:
            nodes = set(update)
            edges = []
            for rule in rules:
                if rule[0] in nodes and rule[1] in nodes:
                    edges.append((rule[0], rule[1]))
            try:
                ordered_nodes = topological_sort(nodes, edges)
            except Exception as e:
                continue
            position = {page: idx for idx, page in enumerate(ordered_nodes)}
            update = sorted(update, key=lambda x: position[x])
            middle_page = update[len(update)//2]
            r += middle_page
    return r

def parse_input(input_path):
    input_raw = open(input_path, "r")
    rules, updates = input_raw.read().split("\n\n")
    rules = [tuple(map(int, line.split("|"))) for line in rules.split("\n")]
    updates = [list(map(int, line.split(","))) for line in updates.split("\n")]
    return rules, updates


def main():
    rules, updates = parse_input("input.txt")
    print("Part 1: ", part_one(rules, updates))
    print("Part 2: ", part_two(rules, updates))


if __name__ == "__main__":
    main()
