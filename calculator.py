
def convert(value):
    value = value.strip().upper()

    if value.endswith("B"):
        return float(value[:-1]) * 1_000_000_000
    elif value.endswith("M"):
        return float(value[:-1]) * 1_000_000
    elif value.endswith("K"):
        return float(value[:-1]) * 1_000
    else:
        return float(value)

def format_num(num):
    if num >= 1_000_000_000:
        return f"{num/1_000_000_000:.2f}B"
    elif num >= 1_000_000:
        return f"{num/1_000_000:.2f}M"
    elif num >= 1_000:
        return f"{num/1_000:.2f}K"
    else:
        return str(int(num))

# ---------------- FLIP MODE ----------------
def flip_mode():
    money = convert(input("Enter your money: "))
    buy_price = convert(input("Buy price (orders): "))
    sell_price = convert(input("Sell price (AH): "))

    amount = int(money // buy_price)

    total_cost = amount * buy_price
    total_revenue = amount * sell_price
    profit = total_revenue - total_cost
    final_money = money + profit

    print("\n--- FLIP RESULTS ---")
    print("Items you can buy:", amount)
    print("Profit:", format_num(profit))
    print("Final money:", format_num(final_money))

# ---------------- LOGS → CHESTS ----------------
def logs_mode():
    money = convert(input("Enter your money: "))
    log_price = convert(input("Price per log: "))
    chest_price = convert(input("Sell price per chest: "))

    logs = int(money // log_price)
    chests = logs // 2

    total_cost = logs * log_price
    total_revenue = chests * chest_price
    profit = total_revenue - total_cost
    final_money = money + profit

    print("\n--- LOGS → CHESTS RESULTS ---")
    print("Logs bought:", logs)
    print("Chests made:", chests)
    print("Profit:", format_num(profit))
    print("Final money:", format_num(final_money))

# ---------------- MENU ----------------
def main():
    print("\n=== TRADING CALCULATOR ===")
    print("1. Flip (AH ↔ Orders)")
    print("2. Logs → Chests")

    choice = input("Choose (1 or 2): ")

    if choice == "1":
        flip_mode()
    elif choice == "2":
        logs_mode()
    else:
        print("Invalid choice")

main()