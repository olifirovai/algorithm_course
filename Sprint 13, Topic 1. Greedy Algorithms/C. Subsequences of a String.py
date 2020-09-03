'''
There are 2 lines, and you need to figure out if the first is a subsequence
of the second.

Input format
The first line contains the string s.
The second line contains string t.
Both lines are made up of small Latin letters.

Output format
Print True if s is a subsequence of t, otherwise False.
'''

def main():
    string_s = input()
    string_t = input()
    s_index = 0
    t_index = 0
    len_s = len(string_s)
    len_t = len(string_t)
    while s_index < len_s and t_index < len_t:
        if string_s[s_index] == string_t[t_index]:
            s_index += 1
        t_index += 1

    return s_index == len_s


if __name__ == '__main__':
    print(main())
