faces_on_die = 6

total_combinations = faces_on_die * faces_on_die
print("Total combinations possible:", total_combinations)

print("\nDistribution of possible combinations:")
combinations_matrix = [[0] *  faces_on_die for _ in range( faces_on_die)]
for i in range( faces_on_die ):
    for j in range( faces_on_die ):
        combinations_matrix[i][j] = (i+1, j+1)

for row in combinations_matrix:
    print(row)
import numpy as np

sum = np.empty((6, 6), dtype=int)
for i in range(1, 7):
    for j in range(1, 7):
        sum[i-1][j-1] = i + j

print("\nProbability of all possible sums:")
for i in range(2, 13):
    count = 0
    for row in sum:
        for value in row:
            if i == value:
                count += 1
    probability = count / total_combinations
    print("P(Sum = {}) = {:.4f}".format(i,probability))
