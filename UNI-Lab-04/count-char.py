myString = input("Enter a the sentence: ")

# remove function


def remove(str):
    return ''.join(str.split())


#  count chars in string
def count_chars(str):
    str = remove(str)
    count = 1
    for i in str:
        count += 1

    return count


print(count_chars(myString))
