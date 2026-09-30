def solution(a):
    visited = set()
    jumps = 0
    index = 0
    while 0 <= index < len(a):
        if index in visited:
            return -1
        visited.add(index)
        index += a[index]
        jumps += 1
    return jumps