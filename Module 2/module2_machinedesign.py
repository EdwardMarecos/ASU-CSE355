from cse355_machine_design import DFA, registry


def problem1():
    """
    L_1 = {w in {0,1}* | w contains 010 as a substring}
    """

    Q = {"qa", "q0", "q01", "q010"}
    Sigma = {"0", "1"}
    delta = {
        ("qa", "0"):"q0",
        ("qa", "1"):"qa",
        ("q0", "0"):"q0",
        ("q0", "1"):"q01",
        ("q01", "0"):"q010",
        ("q01", "1"):"qa",
        ("q010", "0"):"q010",
        ("q010", "1"):"q010",
    }
    q0 = "qa"
    F = {"q010"}

    return DFA(Q, Sigma, delta, q0, F)


def problem2():
    """
    L_2 = {w in {0,1}* | w does not contain 100 as a substring}
    """

    Q = {"qa", "q1", "q0", "q10", "q100"}
    Sigma = {"0", "1"}
    delta = {
        ("qa", "0"):"q0",
        ("qa", "1"):"q1",
        ("q0", "0"):"q0",
        ("q0", "1"):"q1",
        ("q1", "1"):"q1",
        ("q1", "0"):"q10",
        ("q10", "0"):"q100",
        ("q10", "1"):"q1",
        ("q100", "0"):"q100",
        ("q100", "1"):"q100",
    }
    q0 = "qa"
    F = {"qa", "q0", "q1", "q10"}

    return DFA(Q, Sigma, delta, q0, F)


def problem3():
    """
    L_3 = {w in {a,b}* | |w| < 4}
    """

    Q = {"q0", "q1", "q2", "q3", "q4"}
    Sigma = {"a", "b"}
    delta = {
        ("q0", "a"):"q1",
        ("q0", "b"):"q1",
        ("q1", "a"):"q2",
        ("q1", "b"):"q2",
        ("q2", "a"):"q3",
        ("q2", "b"):"q3",
        ("q3", "a"):"q4",
        ("q3", "b"):"q4",
        ("q4", "a"):"q4",
        ("q4", "b"):"q4",
    }
    q0 = "q0"
    F = {"q0", "q1", "q2", "q3"}

    return DFA(Q, Sigma, delta, q0, F)


def problem4():
    """
    L_4 = {w in {a,b,c}* | w has an even number of b's}
    """

    Q = {"q0", "qbe", "qbo"}
    Sigma = {"a", "b", "c"}
    delta = {
        ("q0", "a"):"qbe",
        ("q0", "b"):"qbo",
        ("q0", "c"):"qbe",
        ("qbe", "a"):"qbe",
        ("qbe", "b"):"qbo",
        ("qbe", "c"):"qbe",
        ("qbo", "a"):"qbo",
        ("qbo", "b"):"qbe",
        ("qbo", "c"):"qbo",
    }
    q0 = "q0"
    F = {"q0", "qbe"}

    return DFA(Q, Sigma, delta, q0, F)


def problem5():
    """
    L_5 = {epsilon, 0, 101} on Sigma = {0, 1}
    """

    Q = {"qe", "q0", "q1", "q10","q101","qr"}
    Sigma = {"0", "1"}
    delta = {
        ("qe", "1"):"q1",
        ("qe", "0"):"q0",
        ("q0", "1"):"qr",
        ("q0", "0"):"qr",
        ("q1", "1"):"qr",
        ("q1", "0"):"q10",
        ("q10", "1"):"q101",
        ("q10", "0"):"qr",
        ("q101", "1"):"qr",
        ("q101", "0"):"qr",
        ("qr", "1"):"qr",
        ("qr", "0"):"qr"
    }
    q0 = "qe"
    F = {"qe", "q0", "q101"}

    return DFA(Q, Sigma, delta, q0, F)


def problem6():
    """
    L_6 = {w in {1}* | |w| is a multiple of 2 or 3}
    """

    Q = {"q23", "q1", "q2", "q3", "q4", "q5"}
    Sigma = {"1"}
    delta = {
        ("q23", "1"):"q1",
        ("q1", "1"):"q2",
        ("q2", "1"):"q3",
        ("q3", "1"):"q4",
        ("q4", "1"):"q5",
        ("q5", "1"):"q23",
    }
    q0 = "q23"
    F = {"q23", "q2", "q3", "q4"}

    return DFA(Q, Sigma, delta, q0, F)


def problem7():
    """
    L_7 = {w in {a,b}* | w has an even number of a's, contains aab as a
                         substring, or both}
    """

    Q = {"q0", "qa", "qaa", "qab", "qaaa", "qaab", "qaba", "qabaa", "qabab"}
    Sigma = {"a", "b"}
    delta = { 
        ("q0", "a"):"qa",
        ("q0", "b"):"q0",
        ("qa", "a"):"qaa",
        ("qa", "b"):"qab",

        ("qaa", "a"):"qaaa",
        ("qaa", "b"):"qaab",
        ("qab", "a"):"qaba",
        ("qab", "b"):"qab",

        ("qaaa", "a"):"qaa",
        ("qaaa", "b"):"qaab", 
        ("qaab", "a"):"qaab",
        ("qaab", "b"):"qaab",
        ("qaba", "a"):"qabaa",
        ("qaba", "b"):"qabab",

        ("qabaa", "a"):"qaa",
        ("qabaa", "b"):"qaab",
        ("qabab", "a"):"qa",
        ("qabab", "b"):"q0",
    }
    q0 = "q0"
    F = {"q0", "qaa", "qaab", "qaba", "qabab"}

    return DFA(Q, Sigma, delta, q0, F)


if __name__ == "__main__":
    problem1().submit_as_answer(1)
    problem2().submit_as_answer(2)
    problem3().submit_as_answer(3)
    problem4().submit_as_answer(4)
    problem5().submit_as_answer(5)
    problem6().submit_as_answer(6)
    problem7().submit_as_answer(7)
    registry.export_submissions()
