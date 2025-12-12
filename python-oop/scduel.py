class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def cast_fireball(self, target, fireball_cost, fireball_damage):
        if fireball_cost > self.mana:
            raise Exception(f"{self.name} cannot cast fireball")
        else:
            self.mana -= fireball_cost
            target.get_fireballed(fireball_damage)

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def get_fireballed(self, fireball_damage):
        fireball_damage -= self.__stamina
        self.health -= fireball_damage

    def drink_mana_potion(self, potion_mana):
        potion_mana += self.__intelligence
        self.mana += potion_mana

run_cases = [
    {
        "wizard1_name": "Merlin",
        "wizard1_stamina": 10,
        "wizard1_intelligence": 10,
        "wizard2_name": "Morgana",
        "wizard2_stamina": 8,
        "wizard2_intelligence": 8,
        "fireball_cost": 50,
        "fireball_damage": 30,
        "expect_success": True,
        "expected_wizard1_mana_after": 50,
        "expected_wizard2_alive": True,
    },
    {
        "wizard1_name": "Gandalf",
        "wizard1_stamina": 15,
        "wizard1_intelligence": 12,
        "wizard2_name": "Saruman",
        "wizard2_stamina": 10,
        "wizard2_intelligence": 9,
        "fireball_cost": 80,
        "fireball_damage": 50,
        "expect_success": True,
        "expected_wizard1_mana_after": 40,
        "expected_wizard2_alive": True,
    },
]

submit_cases = run_cases + [
    {
        "wizard1_name": "Harry",
        "wizard1_stamina": 5,
        "wizard1_intelligence": 1,
        "wizard2_name": "Voldemort",
        "wizard2_stamina": 2,
        "wizard2_intelligence": 15,
        "fireball_cost": 200,
        "fireball_damage": 400,
        "expect_success": False,
        "expected_wizard1_mana_after": 10,
        "expected_wizard2_alive": True,
    },
    {
        "wizard1_name": "Ron",
        "wizard1_stamina": 5,
        "wizard1_intelligence": 7,
        "wizard2_name": "Hermione",
        "wizard2_stamina": 2,
        "wizard2_intelligence": 15,
        "fireball_cost": 70,
        "fireball_damage": 400,
        "expect_success": True,
        "expected_wizard1_mana_after": 0,
        "expected_wizard2_alive": False,
    },
]


def test(case):
    print("---------------------------------")
    print(
        f"{case['wizard1_name']} (Stamina: {case['wizard1_stamina']}, Intelligence: {case['wizard1_intelligence']})"
    )
    wizard1 = Wizard(
        case["wizard1_name"], case["wizard1_stamina"], case["wizard1_intelligence"]
    )
    print(f"  Starting health: {wizard1.health}")
    print(f"  Starting mana:   {wizard1.mana}")

    wizard2 = Wizard(
        case["wizard2_name"], case["wizard2_stamina"], case["wizard2_intelligence"]
    )
    print(
        f"{case['wizard2_name']} (Stamina: {case['wizard2_stamina']}, Intelligence: {case['wizard2_intelligence']})"
    )
    print(f"  Starting health: {wizard2.health}")
    print(f"  Starting mana:   {wizard2.mana}")
    print("")

    initial_wizard1_mana = wizard1.mana
    initial_wizard2_health = wizard2.health

    try:
        wizard1.cast_fireball(wizard2, case["fireball_cost"], case["fireball_damage"])
        success = True
        print(f"{case['wizard1_name']} cast fireball at {case['wizard2_name']}...")
        print(f"  Fireball cost:   {case['fireball_cost']}")
        print(f"  Fireball damage: {case['fireball_damage']}")
        print("")
    except Exception as e:
        success = False
        print(f"Exception: {e}")

    wizard1_mana_after = wizard1.mana
    wizard2_alive_after = wizard2.is_alive()

    print(f"Expected cast success: {case['expect_success']}")
    print(f"Actual cast success:   {success}")
    print(
        f"Expected {case['wizard1_name']} mana after: {case['expected_wizard1_mana_after']}"
    )
    print(f"Actual {case['wizard1_name']} mana after:   {wizard1_mana_after}")
    print(
        f"Expected {case['wizard2_name']} alive after: {case['expected_wizard2_alive']}"
    )
    print(f"Actual {case['wizard2_name']} alive after:   {wizard2_alive_after}")

    if success != case["expect_success"]:
        return False
    if wizard1_mana_after != case["expected_wizard1_mana_after"]:
        return False
    if wizard2_alive_after != case["expected_wizard2_alive"]:
        return False
    return True


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for case in test_cases:
        correct = test(case)
        if correct:
            print("Pass")
            passed += 1
        else:
            print("Fail")
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
