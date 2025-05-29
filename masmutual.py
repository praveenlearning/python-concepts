import re


def question_1():
    """
    extract 14 digits from string
    """
    pattern = re.compile(".*(\d{14}).*")
    subject = "Resource/static_37237689138913.xlsx"

    print(pattern.match(subject).group(1))
    print(pattern.sub(r"\1", subject))
    print(pattern.search(subject).group(1))
    print(re.search("(\d{14})", subject).group(1))
    print(pattern.findall(subject))

def question_2():
    s = "randomstring"

    res = ""
    for c in s:
        if c not in ('a', 'e', 'i', 'o', 'u'):
            res += c

    print(res)

    print("".join((c for c in s if c.lower() not in "aeiou")))

if __name__ == '__main__':
    question_1()
    question_2()

    """
    A           B
    1           1
    1           1
    1           1
    1           1

    #lj
    #rj
    #ij
    #fj

    primary key
    unique key
    foreign key
    surrogate key


    How to optimise long running query?


    Round-2: Techno Managerial
    """
