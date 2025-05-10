
def reverse_words(str):
    words = [word for word in str.split('.') if word]
    words.reverse()
    return '.'.join(words)
if __name__ == "__main__":
    str = "blue of sky."
    print(reverse_words(str))