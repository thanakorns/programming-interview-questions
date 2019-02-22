def order(projects):
    listBuild = []
    for project in projects:
        if project.getDepdencies() == 0:
            listBuild.append(project)
    while toBeProcessed(projects) != None or len(listBuild) < len(projects):
        current = toBeProcessed(project)
        for child in current.children():
            child.removeDependencyFrom(current)
            if child.getDependencies() == 0:
                listBuild.append(child)
    if len(listBuild) < len(projects):
        return 'Invalid'
    return listBuild

# basically do DFS on every node, add node in stack to get correct build order.
# stack is valid because the first stuff that is pushed into the stack will be built last and it is not depended by anyone
# this is called topological sort: linearly ordering the vertices in a graph such that for
# every edge (a, b), a appears before b in the linear order.
def orderDFS(projects):
    stack = []
    for project in projects:
        if not orderDFS_helper(project, stack):
            return False
    return stack

def orderDFS_helper(project, stack):
    if project.state == state.PARTIAL:
        return False
    if project.state == state.BLANK:
        for child in project.children:
            if not orderDFS_helper(child, stack):
                return False
        stack.push(project)
        project.setState(state.COMPLETE)
    return True


