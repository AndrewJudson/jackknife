import sys

def probabilities(array, probability_dict):
    cur_prev = [10, 11]
    i = 1
    while i < len(array):
        new_prev = []
        for j in xrange(0, len(cur_prev)):
            new_prev.append(add_probability(cur_prev[j], array[i], probability_dict))
        cur_prev = [k for j in range(len(new_prev)) for k in new_prev[j]]
        i += 1
    return probability_dict

def add_probability(prev, p, probability_dict):
    prev_prob =  probability_dict[prev]
    new_0 = prev * 10
    new_1 = prev * 10 + 1
    probability_dict[new_0] = prev_prob * (1-p)
    probability_dict[new_1] = prev_prob * 1
    return new_0, new_1

def sum_threshold(probability_dict, threshold):
    count = 0
    for key in probability_dict:
        if probability_dict[key] > threshold:
            count += 1
    return count
        
def main():
    array = [float(sys.argv[i]) for i in range(2, len(sys.argv))]
    probability_dict = {10: 1 - array[0], 11: array[0]}
    probabilities(array, probability_dict)
    to_delete = []
    for key in probability_dict:
        if len(str(key)) < len(array) + 1:
            to_delete.append(key)
    for key in to_delete:
        del probability_dict[key]
    print probability_dict
    print sum_threshold(probability_dict, float(sys.argv[1]))
if __name__ == "__main__":
    main()
