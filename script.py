import csv
import sys

def parse_csv(filename):
    f = open(filename, 'rb')
    reader = csv.reader(f)
    header = reader.next()
    exception_message = """Your csv header was named incorrectly, 
                           make sure there are no uneccessary commas 
                           or spaces and that they're in correct order."""
    if header != ['trials', 'probabilities']:
        raise Exception(exception_message)
    trials = []
    probabilities = []
    for row in reader:
        trials.append(int(row[0]))
        probabilities.append(float(row[1]))
    threshold = sum([a * (1-b) for a, b in zip(trials, probabilities)])
    return threshold, probabilities
    
def probabilities(array, probability_dict, sum_dict):
    cur_prev = [10, 11]
    i = 1
    while i < len(array):
        new_prev = []
        for j in xrange(0, len(cur_prev)):
            new_prev.append(add_probability(cur_prev[j], array[i], probability_dict, sum_dict))
        cur_prev = [k for j in range(len(new_prev)) for k in new_prev[j]]
        i += 1
    return probability_dict

def add_probability(prev, p, probability_dict, sum_dict):
    prev_prob =  probability_dict[prev]
    prev_sum = sum_dict[prev]
    new_0 = prev * 10
    new_1 = prev * 10 + 1
    probability_dict[new_0] = prev_prob * (1-p)
    probability_dict[new_1] = prev_prob * p
    sum_dict[new_0] = prev_sum
    sum_dict[new_1] = prev_sum + (1 - p)
    return new_0, new_1

def sum_threshold(sum_dict, probability_dict, threshold):
    count = 0
    for key in sum_dict:
        if sum_dict[key] >= threshold:
            count += probability_dict[key]
    return count
        
def main():
    filename = sys.argv[1]
    threshold, array = parse_csv(filename)
    probability_dict = {10: 1 - array[0], 11: array[0]}
    sum_dict = {10: 0, 11: 1 - array[0]}
    probabilities(array, probability_dict, sum_dict)
    to_delete = []
    for key in probability_dict:
        if len(str(key)) < len(array) + 1:
            to_delete.append(key)
    for key in to_delete:
        del probability_dict[key]
        del sum_dict[key]
    # Should probably combine these in one dictionary
    print sum_threshold(sum_dict, probability_dict, threshold)

if __name__ == "__main__":
    main()
