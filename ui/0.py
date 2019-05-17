friends = {'0': {'222': '关羽'}, '1': {'333': '张飞'}}
for i in range(len(friends)):
    print(friends[str(i)])
    for id, name in friends[str(i)].items():
        print(id, name)