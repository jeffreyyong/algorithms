'''
n = int(input())

for i in range(n):
    a, b = input().strip().split(' ')
    print(int(a) + int(b))
'''




def checksum(card_number):
    def digits(n):
        return [int(d) for d in str(n)]
    numbers = digits(card_number)
    odd_numbers = numbers[-1::-2]
    even_numbers = numbers[-2::-2]
    checksum = 0
    checksum += sum(odd_numbers)
    for even_number in even_numbers:
        checksum += sum(digits(even_number * 2))
    return checksum % 10

def is_card_valid(card_number):
    return checksum(card_number) == 0
