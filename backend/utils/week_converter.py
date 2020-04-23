from datetime import date, timedelta


def week_number_to_date_range(week_number):
    if not week_number:
        week_number = date.today().isocalendar()[1]

    start_of_week = date.fromisocalendar(
        year=date.today().year, week=week_number, day=1)
    end_of_week = start_of_week + timedelta(days=6)

    return (start_of_week, end_of_week)
