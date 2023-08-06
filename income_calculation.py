def calculate_total(income):
    total = 0
    for i in income:
        total = total + i
    return total

riad_inc = [1020,3045,1534,6654,6565,2456,3698,6563,4534,9962]
sagor_inc = [635,4664,4506,2405,869,485,213,466,9711,9664]
dipu_inc = [5000,1533,46636,876,9987,5632,4589,2336,4962,48696]

riad = calculate_total(riad_inc)
sagor = calculate_total(sagor_inc)
dipu = calculate_total(dipu_inc)

print("Riad total income ",riad)
print("Sagor total income ",sagor)
print("Dipu total income ",dipu)