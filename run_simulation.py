import tree_generation
import tree_evolution
import render_tree
import numpy as np

tree_population = []

def generate_tree_population(num_Trees):
    Trees = []
    for i in range(num_Trees):
        Trees.append(tree_generation.generate_tree_properties())

    return Trees


def get_population():
    return tree_population


def generate_sun_cycle(percent):
    #500 days
    sun_cycle = []
    for i in range(500):
        decide = np.random.randint(low = 0, high= 100)
        if decide <= percent:
            sun_cycle.append(1)
        else:
            sun_cycle.append(0)
    return sun_cycle

def generate_rain_cycle(percent):
        #500 days
    rain_cycle = []
    for i in range(500):
        decide = np.random.randint(low = 0, high= 100)
        if decide <= percent:
            rain_cycle.append(1)
        else:
            rain_cycle.append(0)
    return rain_cycle


def simulate_cycle(tree_pop):
    sun_cycle = generate_sun_cycle(80)
    rain_cycle = generate_rain_cycle(30)

    light_produced = 100000
    water_produced = 1000000

    tree_fitness = []

    for tree in tree_pop:
        light_needed = (tree['numLeaves'] ) + (tree['Trunk'][0][0]/2 ) + (tree['numBranches'] / 2)
        water_needed = (tree['numLeaves']  ) + (tree['Trunk'][0][1] * 10) + (tree['numBranches'])

        water_storage = (1/4) * ( tree['Trunk'][0][0] * tree['Trunk'][0][1])
        light_storage = tree['numLeaves'] * 4

        health = 20
        fitness_score = 0

        #iterate through all 500 days
        #break if the tree dies
        for i in range(500):
            if health < 0:
                tree_fitness.append(i)
                break

            #sunny day
            if sun_cycle[i] == 1:
                light_storage = tree['numLeaves']
                if tree['numLeaves'] == 0:
                    light_absorbtion = 0
                else:
                    light_absorbtion = tree['numLeaves'] * 2
                if light_absorbtion < light_needed:
                    health -= 1
            else:
                if tree['numLeaves'] == 0:
                    light_absorbtion = 0
                else:
                    light_absorbtion = light_storage

                if light_absorbtion < light_needed:
                    health -= 1
                light_storage -= light_needed


            #rainy day
            if rain_cycle[i] == 1:
                water_storage = (1/8) * ( tree['Trunk'][0][0] * tree['Trunk'][0][1])
                water_absorbtion = ( tree['Trunk'][0][0] * tree['Trunk'][0][1]) /10
                if water_absorbtion < water_needed:
                    health -= 1
            else:
                water_absorbtion = water_storage
                if water_absorbtion < water_needed:
                    health -= 1
                water_storage -= water_needed
        if health >= 0:
            tree_fitness.append(i)


    return tree_fitness



render_tree.render_trees()
