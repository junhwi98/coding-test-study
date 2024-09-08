import sys
n = int(input())

queue = []
for _ in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        queue.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)

    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])