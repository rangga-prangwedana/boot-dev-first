class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.name = name
        self.health = self.__stamina * 100
        self.mana = self.__intelligence * 10

run_cases = [
    ("Merlin", 10, 10, 1000, 100),
    ("Morgana", 20, 5, 2000, 50),
]

submit_cases = run_cases + [
    ("Arthur", 3, 3, 300, 30),
]


def test(
    wizard_name,
    wizard_stamina,
    wizard_intelligence,
    expected_health,
    expected_mana,
):
    print("---------------------------------")
    print("Creating wizard with:")
    wizard = Wizard(wizard_name, wizard_stamina, wizard_intelligence)
    print(f"  Name: {wizard.name}")
    print(f"  Stamina: {wizard_stamina}")
    print(f"  Intelligence: {wizard_intelligence}")
    print("After initialization:")
    print(f"  Expected mana: {expected_mana}")
    print(f"  Actual mana:   {wizard.mana}")
    print(f"  Expected health: {expected_health}")
    print(f"  Actual health:   {wizard.health}")
    if wizard.mana != expected_mana:
        return False
    if wizard.health != expected_health:
        return False
    isPrivate = True
    try:
        wizard.stamina
        isPrivate = False
        print("Stamina isn't private!")
    except AttributeError:
        pass
    try:
        wizard.intelligence
        isPrivate = False
        print("Intelligence isn't private!")
    except AttributeError:
        pass
    return isPrivate


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
