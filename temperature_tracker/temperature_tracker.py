class TempTracker:

    def __init__(self):

        # for mode
        self.occurrences = [0] * (111) # list of 0s at indices 0..110
        self.max_occurences = 0
        self.mode = None

        # for mean
        self.total_numbers = 0
        self.total_sum = 0.0 # mean should be float
        self.mean = None

        # for min and max
        self.min_temp = float('inf')
        self.max_temp = float('-inf')

    def insert(self, temperature):

        # for mode
        self.occurrences[temperature] += 1
        if self.occurrences[temperature] > self.max_occurrences:
            self.mode = temperature
            self.max_occurrences = self.occurrences[temperature]

        # for mean
        self.total_numbers += 1
        self.total_sum += temperature
        self.mean = self.total_sum / self.total_numbers

        # for min and max
        if temperature > self.max_temp:
            self.max_temp = temperature
        if temperature < self.min_temp:
            self.min_temp = temperature

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode


# Complexity
# O(1) time for each function, and O(1) space related to input! (Our occurrences list's size is bounded by our range of possible temps, in this case 0-110)
