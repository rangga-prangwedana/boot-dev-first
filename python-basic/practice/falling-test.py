from math import isclose

def avg_luck_boost(luck_boosts):
    if len(luck_boosts) < 1:
        return 0.0
    total = 0
    for boost in luck_boosts:
        total += boost
    return total / len(luck_boosts)



run_cases = [
    {
        "luck_boosts": [5, 3, 10],
        "expected_avg": 6.0,
    },
    {
        "luck_boosts": [7],
        "expected_avg": 7.0,
    },
    {
        "luck_boosts": [4, 4, 4],
        "expected_avg": 4.0,
    },
    {
        "luck_boosts": [2, 3],
        "expected_avg": 2.5,
    },
    {
        "luck_boosts": [],
        "expected_avg": 0.0,
    },
]



def test(luck_boosts: list[int], expected_avg: float) -> bool:
    print("---------------------------------")
    print(f"Party luck boosts: {luck_boosts}")

    try:
        avg = avg_luck_boost(luck_boosts)
    except ZeroDivisionError as err:
        print(f"Caught ZeroDivisionError: {err}")
        return False

    print(f"Expected average boost: {expected_avg}")
    print(f"Actual average boost:   {avg}")
    if isclose(avg, expected_avg):
        print("Pass")
        return True

    print("Fail")
    return False


def main() -> None:
    passed = 0
    failed = 0

    for case in run_cases:
        correct = test(**case)
        if correct:
            passed += 1
        else:
            failed += 1

    print()

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")

    print(f"{passed} passed, {failed} failed")


main()
