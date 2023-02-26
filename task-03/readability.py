def countAvgLetters(para):
    words = 0
    a = para.split()
    for i in para:
        if i.isalpha():
            words += 1
    result = words/len(a)
    result = result * 100
    return result
def countAvgSentences(para):
    a = 0
    for i in para:
        if i in ".!":
            a += 1
    b = len(para.split())
    return a*100/b
def main():
    txt = input("Text: ")
    L = countAvgLetters(txt)
    S = countAvgSentences(txt)
    Index = round(0.0588 * L - 0.296 * S - 15.8)
    if Index < 1:
        print("Before Grade 1")
    elif Index > 16:
        print("Grade 16+")
    else:
        print("Grade ",Index)

if __name__ == "__main__":
    main()
