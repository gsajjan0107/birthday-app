import datetime as dt

def is_leap(year: int) -> bool:
    """Check if a given year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def month_day_diff(start: dt.date, end: dt.date) -> tuple[int, int]:
    """Return exact difference in months and days between two dates."""
    months = (end.year - start.year) * 12 + (end.month - start.month)

    if end.day < start.day:
        months -= 1
        prev_month = end.month - 1 or 12
        prev_year = end.year if end.month > 1 else end.year - 1
        last_day_prev_month = (dt.date(prev_year, prev_month + 1, 1) - dt.timedelta(days=1)).day
        days = last_day_prev_month - start.day + end.day
    else:
        days = end.day - start.day

    return months, days

def calculate_age(dob: dt.date, today: dt.date) -> tuple[int, int, int]:
    """Calculate exact age in years, months, and days."""
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    if days < 0:
        months -= 1
        prev_month = today.month - 1 or 12
        prev_year = today.year if today.month > 1 else today.year - 1
        last_day_prev_month = (dt.date(prev_year, prev_month + 1, 1) - dt.timedelta(days=1)).day
        days += last_day_prev_month

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def next_birthday() -> None:
    separators = ["-", "/", ".", ":"]
    formats = [f"%Y{sep}%m{sep}%d" for sep in separators] + \
              [f"%d{sep}%m{sep}%Y" for sep in separators]

    while True:
        dob_str = input("Enter your date of birth (DD-MM-YYYY or YYYY/MM/DD): ")

        dob = None
        for f in formats:
            try:
                dob = dt.datetime.strptime(dob_str, f).date()
                break
            except ValueError:
                continue

        if dob is None:
            print("❌ Invalid format. Try again with a proper date.\n")
            continue

        today = dt.date.today()

        # 🎯 Show Age
        years, months, days = calculate_age(dob, today)
        print(f"🧑 Your current age is: {years} year(s), {months} month(s), and {days} day(s).")

        # 🎯 Next Birthday
        try:
            nxt_bdy = dt.date(today.year, dob.month, dob.day)
        except ValueError:
            if dob.month == 2 and dob.day == 29:
                nxt_bdy = dt.date(today.year, 2, 29) if is_leap(today.year) else dt.date(today.year, 2, 28)
            else:
                print("❌ Invalid date in DOB.\n")
                continue

        if nxt_bdy < today:
            try:
                nxt_bdy = dt.date(today.year + 1, dob.month, dob.day)
            except ValueError:
                nxt_bdy = dt.date(today.year + 1, 2, 29) if is_leap(today.year + 1) else dt.date(today.year + 1, 2, 28)

        days_left = (nxt_bdy - today).days

        if days_left == 0:
            print("🎂 Today is your birthday! Happy Birthday 🎉🥳\n")
        else:
            months, days = month_day_diff(today, nxt_bdy)
            if months > 0:
                print(f"🎉 Your next birthday is in {months} month(s) and {days} day(s).\n")
            else:
                print(f"🎉 Your birthday is in {days} day(s).\n")

        break


# Run
next_birthday()
