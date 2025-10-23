def print_calendar():
    days_in_month = int(input("Enter number of days in the month: "))
    start_day = int(input("Enter starting day of the week (0=Sun,...6=Sat): "))

    # Print the header
    print("S  M  T  W  T  F  S")

    # Print empty spaces for days before start_day
    print("   " * start_day, end="")

    for day in range(1, days_in_month + 1):
        # Print the day with width 2, plus a space for separation
        print(f"{day:>2} ", end="")

        # When we reach the end of the week, print newline
        if (start_day + day) % 7 == 0:
            print()

    print()  # Final newline

print_calendar()