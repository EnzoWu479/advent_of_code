class TrialOperators:
    def __init__(self):
        self.results = set()
        pass
    def trial_operators(self, numbers, result, i=1):
        if i >= len(numbers):
            self.results.add(result)
            return
        
        self.trial_operators(numbers, numbers[i] + result, i + 1)
        self.trial_operators(numbers, numbers[i] * result, i + 1)

    
soma_certos = 0

with open("input.txt") as f:
    for line in f:
        result, numbers = line.split(":")
        result = int(result)
        numbers = list(map(int, numbers.strip().split()))
        trial = TrialOperators()
        trial.trial_operators(numbers, numbers[0])
        if result in trial.results:
            soma_certos += result
print(soma_certos)
