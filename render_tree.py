import pygame
import tree_generation
import run_simulation
import tree_evolution
import time

def draw_tree(trees,screen):
    screen.fill((255, 255, 255))

    for tree in trees:
        #Draw the trunk
        trunk_properties = tree['Trunk'][0]

        trunk_height = trunk_properties[0]
        trunk_width = trunk_properties[1]

        pygame.draw.rect(screen, (135,87,0), pygame.Rect(210, 200, trunk_width, trunk_height))

        #Draw the branches
        trunk_branches = tree['Trunk'][2]
        trunk_branch_spawn_points = tree['Trunk'][1]
        for i in range(len(trunk_branches)):
            branch_loc = trunk_branch_spawn_points[i]
            branch_length = tree[trunk_branches[i]][0]
            pygame.draw.rect(screen, (135,87,0), pygame.Rect(210, 200+branch_loc, branch_length, 10))
            pygame.draw.rect(screen, (135,87,0), pygame.Rect(210-branch_length, 200+branch_loc, branch_length, 10))

            #draw the leaves
            branch_leaf_spawn_points = tree[trunk_branches[i]][2]
            for leaves in range(len(branch_leaf_spawn_points)):
                leaf_location = branch_leaf_spawn_points[leaves]
                leaf_size = tree[tree[trunk_branches[i]][3][leaves]][0]
                #Leaf
                pygame.draw.circle(screen, (99,171,9), (210+leaf_location, 200+branch_loc), leaf_size, 100)
                #Leaf Outline
                pygame.draw.circle(screen, (0,0,0), (210+leaf_location, 200+branch_loc), leaf_size, 1)
                #Leaf
                pygame.draw.circle(screen, (99,171,9), (210-leaf_location, 200+branch_loc), leaf_size, 100)
                #Leaf Outline
                pygame.draw.circle(screen, (0,0,0), (210-leaf_location, 200+branch_loc), leaf_size, 1)

    return



def render_trees():
    pygame.init()


    # Set up the drawing window
    screen = pygame.display.set_mode([500, 500])





    #trees = run_simulation.get_population()
    tree_population = []
    tree_population = run_simulation.generate_tree_population(100)

    finished_flag = 0
    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))

        # Draw a solid blue circle in the center
                                                        # x, y , width, height
        #pygame.draw.rect(screen, (0,0,255), pygame.Rect(210, 400, 10, 60))



        time.sleep(1)
        tree_fitness = run_simulation.simulate_cycle(tree_population)

        matched_trees = list(tree_evolution.match_fitness_tree(tree_population,tree_fitness))
        selected_trees = tree_evolution.select_trees(matched_trees)
        new_generation = tree_evolution.reproduce(selected_trees)
        tree_population = new_generation

        print(tree_fitness)

        draw_tree([tree_population[0]],screen)


        # Flip the display
        pygame.display.flip()




    # Done! Time to quit.
    pygame.quit()
