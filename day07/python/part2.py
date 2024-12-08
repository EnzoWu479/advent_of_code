class TrialOperators:
    def __init__(self):
        self.results = set()
        pass
    def trial_operators(self, numbers, result, wanted_result, i=1):
        if i >= len(numbers):
            self.results.add(result)
            return
        res_sum = numbers[i] + result
        res_tim = numbers[i] * result
        res_con = int(str(result) + str(numbers[i]))
        if res_sum <= wanted_result:
            self.trial_operators(numbers, res_sum, wanted_result, i + 1)
        if res_tim <= wanted_result:
            self.trial_operators(numbers, res_tim, wanted_result, i + 1)
        if res_con <= wanted_result:
            self.trial_operators(numbers, res_con, wanted_result, i + 1)

    
soma_certos = 0

with open("input.txt") as f:
    for line in f:
        result, numbers = line.split(":")
        result = int(result)
        numbers = list(map(int, numbers.strip().split()))
        trial = TrialOperators()
        trial.trial_operators(numbers, numbers[0], result)
        if result in trial.results:
            soma_certos += result
print(soma_certos)
