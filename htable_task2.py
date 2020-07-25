from dstructs.hash_table import HashTable

if __name__ == '__main__':
    m = 5
    hash_table = HashTable(m)

    inquiries = [
        ('add', 'world'),
        ('add', 'HellO'), 
        ('check', 4),
        ('find', 'World'),
        ('find', 'world'),
        ('del',  'world'),
        ('check', 4),
        ('del', 'HellO'),
        ('add', 'luck'),
        ('add', 'GooD'),
        ('check', 2),
        ('del', 'good')
    ]
    
    for command, operand in inquiries:

        if command == 'add':
            hash_table.insert(operand)
        if command == 'del':
            hash_table.delete(operand)
        if command == 'find':
            result = hash_table.search(operand)
            if result: print('yes')
            else: print('no')
        if command == 'check':
            lst = hash_table.check(int(operand))
            if len(lst) != 0:
                for i in lst:
                    print(i, end=' ')
            print('\n')

    