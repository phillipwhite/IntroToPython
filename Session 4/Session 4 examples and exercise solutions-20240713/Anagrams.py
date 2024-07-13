def main():
    s1 = input("Enter the first string: ").strip() # Method strip removes leading and trailing whitespace characters from string
    s2 = input("Enter the second string: ").strip()
    print(s1, "and", s2, "are", ("anagrams." if isAnagram(s1, s2) else "not anagrams."))

def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False

    newS1 = sort(s1);
    newS2 = sort(s2);

    return newS1 == newS2

def sort(s):
    r = list(s)
    r.sort()

    result = ""
    for ch in r:
        result += ch

    return result

main()
