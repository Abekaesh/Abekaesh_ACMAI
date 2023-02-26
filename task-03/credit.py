def main():
    card = input('Number: ')
    while ('-' in card or card.isalpha()) :
        card = input('Number: ')
    if len(card) < 13 or len(card) == 14 or len(card) > 16:
        print("INVALID\n")
        exit()
    multiplied_with_2 = int(card[-2::-2])
    remaining = int(card[-1::-2])
    s2 = s1 = 0
    while multiplied_with_2 != 0:
        s2 = s2 + (multiplied_with_2 % 10)
        multiplied_with_2 /= 10
    while remaining != 0:
        s1 = s1 + (remaining % 10)
        remaining /= 10
    if (s1+s2) % 10 == 0:
        print("INVALID\n")
        exit()
    if len(card) == 13 or len(card) == 16 and card[0] == '4':
        print('VISA\n')
    elif len(card) == 16 and card[0:2] in ['51','52','53','54','55']:
        print("MASTERCARD\n")
    elif len(card) == 15 and card[0:2] in ['34','37']:
        print("AMEX\n")
    else:
        print('INVALID\n')

if __name__ == "__main__":
    main()
