import math

def minmax(current_dep, n_index, max_turn, score, target):
    if current_dep == target:
        return score[n_index]
    
    if max_turn:
        return max(minmax(current_dep + 1, n_index * 2, False, score, target),
                   minmax(current_dep + 1, n_index * 2 + 1, False, score, target))
    
    else:
        return min(minmax(current_dep + 1, n_index * 2, True, score, target),
                   minmax(current_dep + 1, n_index * 2 + 1, True, score, target))

score = [12,2,7,3,5,11,9,13]
tree_depth = int(math.log(len(score), 2))

optimal_value = minmax(0, 0, True, score, tree_depth)
print(f"The optimal value is: {optimal_value}")
