import sys
import csv


def main():
    # checks the usage
    if len(sys.argv) < 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")
    else:
        # opening files
        c_file = open(sys.argv[1], "r")
        t_file = open(sys.argv[2], "r")

        seq = {}
        # initialising the seq dictionary to store occurance of respective STR sequence
        reader = csv.reader(c_file)
        for row in reader:
            header = row
            header.pop(0)
            for j in header:
                seq[j] = 0
            break

        c_file.close()

        # to read the dna pattern of some persons from the file
        c = open(sys.argv[1], "r")
        p_read = csv.DictReader(c)
        p = []
        for row in p_read:
            p.append(row)

        sample = t_file.read()

        # recording each pattern occurance into seq
        for key in seq:
            b = longest_match(sample, key)
            seq[key] = b

        # checking matches
        for person in p:
            match = 0
            for key in seq:
                if person[key] == str(seq[key]):
                    match += 1
            if match == len(seq):
                print(person["name"])
                sys.exit()
        print("No match")     # executes when no match is found

# find max no of occurance of a STR sequence


def longest_match(dna, s):
    i = 0
    j = len(s)
    max = 0
    for x in range(len(dna)):
        if dna[i:j] == s:
            tmp = 0
            while dna[i:j] == s:
                tmp += 1
                i += len(s)
                j += len(s)
                if(tmp > max):
                    max = tmp
        else:
            i += 1
            j += 1
    return max


if __name__ == "__main__":
    main()
