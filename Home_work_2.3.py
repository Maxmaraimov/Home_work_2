def powers_of_two(N):
    powers = []
    power = 1
    while power <= N:
        powers.append(power)
        power *= 2
        
    return powers
print(powers_of_two(30))