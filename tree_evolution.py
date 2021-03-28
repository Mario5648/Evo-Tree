import numpy as np

#heredity

def match_fitness_tree(tree_pop , fitness_scores):

    tree_with_fitness = zip(fitness_scores,tree_pop)
    tree_with_fitness = list(tree_with_fitness)
    tree_with_fitness = sorted(tree_with_fitness, key=lambda x: x[0])
    return tree_with_fitness




#Selection

def select_trees(trees):

    selected_trees = []
    chosen = []
    while len(selected_trees) < 50:
        tree_index = np.random.randint(low = 0, high= len(trees))

        r = np.random.randint(low = 0, high= 500)
        if r <= trees[tree_index][0]:
            selected_trees.append(trees[tree_index][1])
            trees.pop(tree_index)

    return selected_trees


#Reproduction/Selection
    #pick 2 parents
    #make a new elements
        #crossover
        #mutation

def reproduce(selected_trees):

    new_generation = []

    for _ in range(100):
        parent1 = np.random.randint(low = 0, high= 49)
        parent2 = np.random.randint(low = 0, high= 49)


        #trunk
        parent = np.random.randint(low=0, high = 1)
        tree = {}
        if parent == 0:
            tree['Trunk'] = selected_trees[parent1]['Trunk'][::]
        else:
            tree['Trunk'] = selected_trees[parent2]['Trunk'][::]

        #branches
        parent = np.random.randint(low=0, high = 1)

        if parent == 0:
            tree['Trunk'][1] = selected_trees[parent1]['Trunk'][1][::]
            tree['Trunk'][2] = selected_trees[parent1]['Trunk'][2][::]
            tree['numBranches'] = selected_trees[parent1]['numBranches']
        else:
            tree['Trunk'][1] = selected_trees[parent2]['Trunk'][1][::]
            tree['Trunk'][2] = selected_trees[parent2]['Trunk'][2][::]
            tree['numBranches'] = selected_trees[parent2]['numBranches']


        #leaves
        parent = np.random.randint(low=0, high = 1)

        iLeaves = 0

        for i in range(tree['numBranches']+1):
            branch = 'B'+str(i)
            parent = np.random.randint(low=0, high = 1)
            if parent == 0 :
                if branch in selected_trees[parent1]:
                    tree[branch]= selected_trees[parent1][branch][::]
                    for j in range(len(selected_trees[parent1][branch][2])):
                        tree['L'+str(iLeaves)] = selected_trees[parent1]['L'+str(iLeaves)]
                        iLeaves+=1
                else:
                    tree[branch]= selected_trees[parent2][branch][::]
                    for j in range(len(selected_trees[parent2][branch][2])):
                        tree['L'+str(iLeaves)] = selected_trees[parent2]['L'+str(iLeaves)]
                        iLeaves += 1

            else:
                if branch in selected_trees[parent2]:
                    tree[branch]= selected_trees[parent2][branch][::]
                    for j in range(len(selected_trees[parent2][branch][2])):
                        tree['L'+str(iLeaves)] = selected_trees[parent2]['L'+str(iLeaves)]
                        iLeaves +=1
                else:
                    tree[branch]= selected_trees[parent1][branch][::]
                    for j in range(len(selected_trees[parent1][branch][2])):
                        tree['L'+str(iLeaves)] = selected_trees[parent1]['L'+str(iLeaves)]
                        iLeaves +=1
        tree['numLeaves'] = iLeaves







        mutation = np.random.randint(low=1, high = 100)

        if mutation <= 50:
            tree['Trunk'][0][0] = tree['Trunk'][0][0] + np.random.randint(low = -10, high = 10)

            tree['Trunk'][0][1] = tree['Trunk'][0][1] + np.random.randint(low = -5, high = 5)

        new_generation.append(tree)

    return new_generation
