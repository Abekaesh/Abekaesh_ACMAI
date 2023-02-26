def main():
    height = int(input("Height: "))
    for i in range(1, height + 1):
        print((height- i)*" "+i*"#"+" "+i*"#" )

if __name__ == "__main__":
    main()
