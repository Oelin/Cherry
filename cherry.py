import math
import random as rnd


def cherry(animal, fitness, cross, mutate, parents, children, rounds):

        # create an initial population

        population = [animal() for _ in range(parents)]


        for round in range(rounds):

                # we're essentially doing a simplified version of tornament
                # selection with crossover

                winners = []
                tornament = population[: children]

                # order tornament members by fitness (lower is better)

                tornament.sort(key=fitness)


                for rank, animal in enumerate(tornament):
                        if lucky(rank): winners.append(animal)


                # create offspring, using the winners as parents

                offspring = []

                for _ in range(children):

                        parent1 = rnd.choice(winners)
                        parent2 = rnd.choice(winners)

                        child = mutate(cross(parent1, parent2))
                        offspring.append(child)


                # finally, introduce the offspring into the population and
                # shuffle

                population[: children] = offspring
                population.sort(key=lambda x: rnd.random())


        return population


def lucky(rank):
        return rnd.random() < 1 / math.sqrt(1 + rank)
