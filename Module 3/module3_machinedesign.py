from cse355_machine_design import NFA, registry


def problem1():
    """
    L_1 = {w in {0,1}* | w contains 1010 as a substring}, five states
    """

    Q = {"q0", "q1", "q2", "q3", "q4"}
    Sigma = {"0", "1"}
    delta = {
        ("q0", "0"): {"q0"},
        ("q0", "1"): {"q1"},
        ("q1", "0"): {"q2"},
        ("q1", "1"): {"q1"},
        ("q2", "0"): {"q0"},
        ("q2", "1"): {"q3"},
        ("q3", "0"): {"q4"},
        ("q3", "1"): {"q1"},
        ("q4", "0"): {"q4"},
        ("q4", "1"): {"q4"}
    }
    q0 = "q0"
    F = {"q4"}

    return NFA(Q, Sigma, delta, q0, F)


def problem2():
    """
    L_2 = {0,1}, two states
    """

    Q = {"q0", "q1"}
    Sigma = {"0", "1"}
    delta = {
        ("q0", "0"): {"q1"},
        ("q0", "1"): {"q1"},
    }
    q0 = "q0"
    F = {"q1"}

    return NFA(Q, Sigma, delta, q0, F)


def problem3():
    """
    L_3 = {w in {a,b}* | w contains a pair of a's separated by an odd # of b's},     four states
    """

    Q = {"q0", "q1", "q2", "q3"}
    Sigma = {"a", "b"}
    delta = {
        ("q0", "a"): {"q1"},
        ("q0", "b"): {"q0"},
        ("q1", "a"): {"q1"},
        ("q1", "b"): {"q2"},
        ("q2", "a"): {"q3"},
        ("q2", "b"): {"q1"},
        ("q3", "a"): {"q3"},
        ("q3", "b"): {"q3"},
    }
    q0 = "q0"
    F = {"q3"}

    return NFA(Q, Sigma, delta, q0, F)


def problem4():
    """
    L_4 = {1^a0^b1^c | a >= 0, b >= 1, c >= 0}, three states
    """

    Q = {"q0", "q1", "q2"}
    Sigma = {"0", "1"}
    delta = {
        ("q0", "0"): {"q1"},
        ("q0", "1"): {"q0"},
        ("q1", "0"): {"q1"},
        ("q1", "1"): {"q2"},
        ("q2", "1"): {"q2"}
    }
    q0 = "q0"
    F = {"q1", "q2"}

    return NFA(Q, Sigma, delta, q0, F)


def problem5():
    """
    L_5 = {w in {0,1}* | w has exactly one 0, an odd # of 1s, or both}, five states
    """

    Q = {"s", "q0", "q1", "p0", "p1"}
    Sigma = {"0", "1"}
    delta = {
        # start
        ("s", "_"): {"q0", "p0"},
        # check for exactly one zero
        ("q0", "1"): {"q0"},
        ("q0", "0"): {"q1"},
        ("q1", "1"): {"q1"},
        # check for odd ones
        ("p0", "1"): {"p1"},
        ("p0", "0"): {"p0"},
        ("p1", "1"): {"p0"},
        ("p1", "0"): {"p1"}
    }
    q0 = "s"
    F = {"q1", "p1"}

    return NFA(Q, Sigma, delta, q0, F)


if __name__ == "__main__":
    problem1().submit_as_answer(1)
    problem2().submit_as_answer(2)
    problem3().submit_as_answer(3)
    problem4().submit_as_answer(4)
    problem5().submit_as_answer(5)
    registry.export_submissions()
