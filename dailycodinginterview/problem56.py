def helper(mat, partial_sol, k):
    if len(partial_sol) == len(mat):
        return True

    for i in range(k):
        partial_sol.append(i)
        if isValid(mat, partial_sol):
            result = helper(mat, partial_sol)
            if result:
                return True
        partial_sol.pop()

    return False

def isValid(mat, partial_sol):
    if len(partial_sol) == 1:
        return True
    last_elem = len(partial_sol)-1
    for i in range(last_elem):
        if mat[last_elem][i] == 1 and partial_sol[last_elem] == partial_sol[i]:
            return False
    return True


def k_most_coloring(mat, k):
    partial_sol = []
    return helper(mat, partial_sol, k)
