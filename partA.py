faces_on_die = 6

total_combinations = faces_on_die * faces_on_die
print("Total combinations possible:", total_combinations)

combinations_matrix = [[0] * faces_on_die for _ in range(faces_on_die)]
for i in range(1, faces_on_die + 1):
    for j in range(1, faces_on_die + 1):
        combinations_matrix[i - 1][j - 1] = i + j

print("\nDistribution of possible combinations:")
for row in combinations_matrix:
    print(row)

probabilities = {}
for sum_val in range(2, 13):
    count = sum(row.count(sum_val) for row in combinations_matrix)
    probabilities[sum_val] = count / total_combinations

print("\nProbability of possible sums:")
for sum_val, prob in probabilities.items():
    print(f"P(Sum = {sum_val}) = {prob:.5f}")
