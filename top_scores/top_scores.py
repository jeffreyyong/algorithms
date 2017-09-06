# Question: Write a function that takes: 1) a list of unsorted_score
#                                        2) the highest_possible_score in the game
# And returns a sorted list of scores in less than O(nlgn) time.

# A greedy algorithm iterates through the problem space taking the optimal solution "so far", until
# it reaches the end.

# The greedy approach is only optimal if the problem has "optimal substructure", which means stitching
# together optimal solutions to subproblem yields an optimal solution


# Counting is a common pattern in time-saving algorithms. It can often get you O(n) runtime, but at the expense
# of adding O(n) space.
# The idea is to define a dictionary of list (call it e.g. counts) where the keys/indices represent the items from 
# the input set and the values represent the number of times the itme appears. In one pass through the input
# you can fully populate the counts:

def main():

    print(sort_scores([37, 89, 41, 65, 91, 53], 100))

def sort_scores(unsorted_scores, highest_possible_score):

    # list of 0s at indices 0..highest_possible_score

    score_counts = [0] * (highest_possible_score + 1)

    print("score_counts", score_counts)


    # populate score_counts

    for score in unsorted_scores:
        score_counts[score] += 1

    # populate the final sorted list
    sorted_scores = []

    # for each item in score_counts
    for score in xrange(len(score_counts) - 1, -1, -1):
        print("score", score)
        count = score_counts[score]

        print("count", count)

        # for the number of times the item occurs
        for time in xrange(count):
            print("time", time/

            # add it to the sorted list
            sorted_scores.append(score)

    return sorted_scores

if __name__ == "__main__":
    main()

# Are we nesting two loops towards the bottom? 
# No! The outer loop runs once for each unique number in the list. The inner loop runs once for each time that number occurred.
# So in essence we're just looping through the n numbers from out input list, except we're splitting it 
# into two steps (1) each unique number, and (2) each time that number appeared

# In each iteration of our two nested loops, we append one item to sorted scores. How many numbers end up in sorted_scores
# in the end? Exactly how many were in our input list n.
