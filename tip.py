import math

def get_number(prompt, minimum=0, cast=float):
    """ Keep asking until the user enters a valid number >= minimum."""
    while True:
        raw = input(prompt).strip()
        try:
            value = cast(raw)
        except ValueError:
            print(" Please enter a valid number.")
            continue
        if value < minimum:
            print(f" Must be at least {minimum}.")
            continue
        return value

def ask_yes_no(prompt):
    return input(prompt).strip().lower() in ("y", "yes")

def choose_tip():
    presets = {"1": 10, "2": 15, "3": 18, "4": 20}
    print("Tip: 1) 10%  2) 15%  3) 18%  4) 20%  5) custom")
    while True:
        choice = input("Choose 1-5: ").strip()
        if choice in presets:
            return presets[choice]
        if choice == "5":
            return get_number("Custom tip %: ", minimum=0)
        print("  Pick a number from 1 to 5.")


def calculate():
    bill = get_number("Bill amount: ", minimum=0.01)
    tip_pct = choose_tip()
    people = get_number("Split between: ", minimum=1, cast=int)

    tip = bill * tip_pct / 100
    total = bill + tip
    each = total / people

    if ask_yes_no("Round each share up to a whole number? (y/n): "):
        each = math.ceil(each)
        total = each * people
        tip = total - bill

    print("\n--- Summary ---")
    print(f"Bill:      {bill:.2f}")
    print(f"Tip:       {tip:.2f} ({tip / bill * 100:.1f}%)")
    print(f"Total:     {total:.2f}")
    print(f"Each pays: {each:.2f}\n")


def main():
    print("=== Tip Calculator ===\n")
    while True:
        calculate()
        if not ask_yes_no("Calculate another? (y/n): "):
            print("Bye!")
            break
        print()

if __name__ == "__main__":
    main()