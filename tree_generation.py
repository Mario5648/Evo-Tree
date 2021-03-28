import numpy as np

def generate_trunk_properties():
    height = np.random.randint(low = 100, high= 300)
    width = np.random.randint(low = 10, high = 30)
    growth_rate = 1
    num_branches = np.random.randint(low = 2, high= 100)
    return [height,width,growth_rate,num_branches]

def generate_branch_properties():
    length_max = np.random.randint(low = 60, high= 100)
    length_min = np.random.randint(low = 20, high= 50)
    growth_rate = 1
    num_leaves = np.random.randint(low = 1, high= 10)
    return [length_max,length_min,growth_rate,num_leaves]

def generate_leaf_properties():
    size_max = np.random.randint(low = 10, high= 15)
    size_min = 8
    growth_rate = 1
    return [size_max,size_min,growth_rate]

def generate_tree_properties():

    trunk_height,trunk_width,trunk_rate,trunk_branches = generate_trunk_properties()
    branch_length_max,branch_length_min, branch_rate, branch_leaves = generate_branch_properties()
    leaf_size_max, leaf_size_min , leaf_rate = generate_leaf_properties()


    tree = {}
    tree['Trunk'] = [[trunk_height,trunk_width,trunk_rate,trunk_branches]]

    #connect branches to the trunk
    branch_spawn_points = []
    branch_connections = []
    for i in range(trunk_branches):
        branch_spawn_points.append(np.random.randint(low = 0, high= 90))
        branch_connections.append('B'+str(i))
        tree['B'+str(i)] = [np.random.randint(low = branch_length_min, high= branch_length_max) , np.random.randint(low = 0, high= branch_leaves)]
    branch_spawn_points.sort()
    tree['Trunk'].append(branch_spawn_points[:])
    tree['Trunk'].append(branch_connections[:])
    tree['numBranches'] = i
    branch_spawn_points = []
    branch_connections = []

    iLeaves = 0
    #connect leaves to the branch
    leaf_spawn_point = []
    leaf_connections = []
    for branch in tree['Trunk'][2]:
        for i in range(tree[branch][1]):
            leaf_spawn_point.append(np.random.randint(low = 10, high= tree[branch][0]))
            leaf_connections.append('L'+str(iLeaves))
            tree['L'+str(iLeaves)] = [np.random.randint(low = leaf_size_min, high= leaf_size_max)]
            iLeaves+=1
        leaf_spawn_point.sort()
        tree[branch].append(leaf_spawn_point[:])
        tree[branch].append(leaf_connections[:])
        leaf_connections = []
        leaf_spawn_point = []

    tree['numLeaves'] = iLeaves

    return tree
