def main():
    prompt = input()
    print(convert(prompt))


def convert(s):
    return s.replace(":)", "🙂").replace(":(", "🙁")


main()
