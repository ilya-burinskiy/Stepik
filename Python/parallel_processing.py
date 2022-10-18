from dstructs.minheap import HeapMin

if __name__ == "__main__":
    s = input().split()
    cpu_num, task_num = int(s[0]), int(s[1])

    tasks = input().split()
    tasks = list(map(int, tasks))

    array = []
    for i in range(cpu_num):
        array.append((0, i))
    
    prior_q = HeapMin(array)
    for task_time in tasks:
        cpu_t, cpu_idx = prior_q.get_min()
        print(cpu_idx, cpu_t)

        prior_q.change_priority(0, (cpu_t + task_time, cpu_idx))
