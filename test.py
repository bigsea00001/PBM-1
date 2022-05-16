rows = [['d', 'ee'], ['333', '3'], ['1111', 'ddddddd']]


_return_row = [None for i in range(len(rows[0]))]
print(_return_row)

elements_row = [1 for i in rows[0]]

for idx_row, row in enumerate(rows):
    for idx_each, each in enumerate(row):
        if len(each) > elements_row[idx_each]:
            _return_row[idx_each] = len(each)

print(_return_row)
