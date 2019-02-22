
'''
yosemite11abc
yosemite011abc


yosemite12
yosemite2a

number smaller than alphabet
compare : a:string -> b:string -> int (0 if equal, 1 if a > b, -1 otherwise)

0-9a-z
'''

def compute_val(num):
    ans = 0
    for n in num:
        ans = ans* 10 + int(n)
    return ans


def find_num(i, a):
    a_start = i
    while i < len(a) and a[i].isDigit():
        i += 1
    a_end = i
    return (a_start, a_end)


def compare(a, b):
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i].isDigit() and b[j].isDigit():
            # computer the values for a and b and do processing to guarantee that you stop before you find number
            a_start, a_end = find_num(i, a)
            b_start, b_end = find_num(j, b)
            a_val = compute_val(a[a_start:a_end])
            b_val = compute_val(b[b_start:b_end])
            if a_val > b_val:
                return 1
            elif a_val < b_val:
                return -1

            if a_end > b_end:
                return 1
            elif a_end < b_end:
                return -1
            i = a_end
            j = b_end
        elif a[i].isDigit() or b[j].isDigit():
            return -1 if a[i] in number else 1
        # if a[i] and b[j] are characters
        else:
            if ord(a[i]) != ord(b[j]):
                return 1 if ord(a[i]) > ord(b[j]) else -1
        i += 1
        j += 1
    if i < len(a):
        return 1
    elif j < len(b):
        return -1
    if i == j:
        return 0
    return 1 if i > j else -1


print(compare('yosemite', 'yosemite'))  # 0, passed
print(compare('yosemite', 'yosemite0'))  # -1, passed
print(compare('yosemite', 'yosemit'))  # 1, passed

print(compare('yosemite11', 'yosemit0011'))  # -1, passed
print(compare('yosemite001', 'yosemite0002'))  # -1, passed
print(compare('yosemite02', 'yosemite0002'))  # -1, passed

print(compare('yosemite02abc', 'yosemite02abc'))  # -1, passed
print(compare('yosemite02abd', 'yosemite02abc'))  # -1, passed
print(compare('yosemite02abc003', 'yosemite02abc000005'))  # -1, passed
print(compare('yosemite0', 'yosemitea'))  # -1, passed










def add_neighbors_2(x, y, d, mat, visited):
  res = []
  for x_offset, y_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    x1, y1 = x + x_offset, y + y_offset
    if (x1, y1) not in visited:
      if x1 >= 0 and x1 <= len(mat)-1 and y1 >= 0 and y1 <= len(mat[0])-1:
        res.append((x1, y1, d+1))
  return res

def attempt2(mat):
  queue = []
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      if mat[i][j] == 0:
        queue.append((i,j,0))
  visited = set()
  ans = -1
  while queue:
    x, y, d = queue.pop(0)
    visited.add((x,y))
    if d > 0:
      ans = max(ans, d)
    queue = queue + add_neighbors_2(x, y, d, mat, visited)
  return ans