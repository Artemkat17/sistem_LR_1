import numpy as np


def create_rank_template(*rankings):
    rank = {}
    counter = 0

    for element in rankings[0]:
        if isinstance(element, list):
            for sub_elem in element:
                rank[sub_elem] = counter
                counter += 1
        else:
            rank[element] = counter
            counter += 1

    return rank


def generate_rank_matrix(rank, *rankings):
    matrix = []
    for ranking in rankings:
        order_list = [0] * len(rank)
        for i, item in enumerate(ranking):
            if isinstance(item, list):
                for sub_item in item:
                    order_list[rank[sub_item]] = i + 1
            else:
                order_list[rank[item]] = i + 1
        matrix.append(order_list)

    return np.array(matrix)


def calculate_similarity_ratio(matrix, num_experts, counter):
    sum_ranks = np.sum(matrix, axis=0)

    D = np.var(sum_ranks) * counter / (counter - 1)
    D_max = (num_experts ** 2) * ((counter ** 3 - counter) / 12) / (counter - 1)

    return format(D / D_max, ".2f")


def task():
    ranking_a = [1, [2, 3], 4, [5, 6, 7], 8, 9, 10]
    ranking_b = [[1, 2], [3, 4, 5], 6, 7, 9, [8, 10]]
    ranking_c = [3, [1, 4], 2, 6, [5, 7, 8], [9, 10]]

    num_experts = len([ranking_a, ranking_b, ranking_c])
    rank = create_rank_template(ranking_a, ranking_b, ranking_c)
    matrix = generate_rank_matrix(rank, ranking_a, ranking_b, ranking_c)
    result = calculate_similarity_ratio(matrix, num_experts, len(rank))

    print(result)


if __name__ == "__main__":
    task()
