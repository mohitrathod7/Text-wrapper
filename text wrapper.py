def wrap(string, max_width):
    chars = []
    output = ""
    i = 0
    j = max_width
    while j < len(string)+max_width :
        chars.append(string[i:j])
        i += max_width
        j += max_width

    for i in chars:
        if chars.index(i) != len(chars)-1:
            output += (i + "\n")
        else:
            output += (i)
    return output


if __name__ == '__main__':
    string = input("Enter a string : ")
    max_width = int(input("To how much characters do you want to wrap ? "))
    result = wrap(string, max_width)
    print(result)
