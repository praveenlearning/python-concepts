from vikas_exam.banking import solution

if __name__ == '__main__':
    n_queries = [
        ["CREATE_ACCOUNT", "1", "account_1"],
        ["CREATE_ACCOUNT", "2", "account_2"],
        ["CREATE_ACCOUNT", "3", "account_3"],
        ["DEPOSIT", "4", "account_1", "2000"],
        ["DEPOSIT", "5", "account_2", "3000"],
        ["DEPOSIT", "6", "account_3", "4000"],
        ["TOP_ACTIVITY", "7", "3"],
        ["PAY", "8", "account_1", "1500"],
        ["PAY", "9", "account_2", "250"],
        ["PAY", "10", "account_3", "250"],
        ["TOP_ACTIVITY", "11", "3"],
    ]
    print(solution(queries=n_queries))

    t = {
        "a": 1
    }

    t.get("a", 0)
    t["a"] = 2
    print(t)
