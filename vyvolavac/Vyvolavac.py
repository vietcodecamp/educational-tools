#!/usr/bin/python
"""
    Vyvolavac.py: Randomly selects a student with a certain probability.
    1st argument input_path - input path of student names with (or without) statistics, input file should contain
    one student per line and the statistics are tab delimited
    2nd argument (optional): output_path  - output path for new statistics  
"""

__maintainer__ = "Dagy Tran"
__version__ = "0.1 beta"
__status__ = "Development"


import sys
from random import randint
import matplotlib.pyplot as plt


def load_statistics(input_path):
    stats = {}
    should_reset = False
    with open(input_path, 'r') as input_file:
        for line in input_file:
            split_line = line.split('\t')

            if len(split_line) == 1:
                stats[split_line[0].strip()] = (0, 0)
                should_reset = True
            elif len(split_line) == 3:
                stats[split_line[0]] = (int(split_line[1]), int(split_line[2]))

    if should_reset:
        stats = reset_stats(stats, 2)

    return stats


def reset_stats(stats_dict, multiplier=2):
    number_of_students = len(stats_dict)

    for key, value in stats_dict.items():
        stats_dict[key] = (0, multiplier * number_of_students)
    return stats_dict


def save_statistics(output_path, stats_dictionary):
    with open(output_path, 'w') as output_file:
        lines = list(map(lambda kv: '{}\t{}\t{}'.format(kv[0], kv[1][0], kv[1][1]), stats_dictionary.items()))
        output_file.write('\n'.join(lines))


def redistribute(stats_dictionary, key):
    new_stats = {}
    number_of_students = len(stats_dictionary)
    if key not in stats_dictionary:
        print('Error: User not in dictionary.')
        return stats_dictionary

    student_points = stats_dictionary[key][1]
    if student_points < number_of_students - 1:
        print('Warning: User {} has not enough points to redistribute. Points {}. Returning unchanged stats'.format(key,
                                                                                                                    student_points))
        return stats_dictionary
    else:
        for k, (count, points) in stats_dictionary.items():
            if k != key:
                new_stats[k] = (count, points + 1)
            else:
                new_stats[k] = (count + 1, points - (number_of_students - 1))

    return new_stats


def select_student(stats_dict):
    cumulative_sum = 0
    for key, (count, points) in stats_dict.items():
        cumulative_sum += points

    selected_student = ""
    selected_index = randint(0, cumulative_sum)
    print(cumulative_sum)
    print(selected_index)
    prefix_sum = 0
    for key, (count, points) in stats_dict.items():
        prefix_sum += points
        if selected_index <= prefix_sum:
            selected_student = key
            break

    return selected_student


def plot_stats(stats):
    keys = []
    counts = []
    points = []

    for key, (count, point) in stats.items():
        keys.append(key)
        counts.append(count)
        points.append(point)

    plt.figure(1)
    plt.subplot(211)
    plt.bar([i for i in range(len(stats))], counts, tick_label=keys)
    plt.xticks([i for i in range(len(stats))], keys, rotation=-45)
    plt.grid()
    plt.ylabel("Selected Count")
    plt.title("Selected Count")

    plt.subplot(223)
    plt.pie(points, labels=keys, autopct='%1.0f%%')
    plt.title("Probabilities")
    plt.tight_layout()
    plt.show()


def main(argv):
    print(argv)
    if len(argv) == 1:
        print("Input file is needed.")
        return
    if len(argv) > 1:
        file_path = argv[1]
        statistics_dictionary = load_statistics(file_path)
        selected_student = select_student(statistics_dictionary)
        print(selected_student)
        new_statistics_dictionary = redistribute(statistics_dictionary, selected_student)
        plot_stats(new_statistics_dictionary)

        if '-s' in argv or '--save' in argv:
            save_statistics(file_path, new_statistics_dictionary)


if __name__ == "__main__":
    main(sys.argv)
