def disemvowel():
    string = input('Escribe la frase que tu quieras:\n')
    for i in "aeiouAEIOU":
        # print(i)
        string = string.replace(i,'')
        # print(string)
    print(string)

if __name__ == "__main__":
    disemvowel()