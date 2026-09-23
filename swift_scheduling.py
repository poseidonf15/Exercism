"""
Module to convert delivery date descriptions to actual delivery dates, based on when the meeting started.
"""
from datetime import datetime, timedelta
import calendar

def delivery_date(start, description):
    """Function to using the time of the start of the meeting and the description return the delivery date.

    Args:
        start (datetime): The time of the start of the meeting.
        description (str): The delivery date description we got from the boss.

    Returns:
        datetime: The delivery date
    """
    dt_start = datetime.fromisoformat(start)
    result = None

    if description == "NOW":
        result = dt_start + timedelta(hours=2)

    elif description == "ASAP":
        if dt_start.hour < 13:
            result = dt_start.replace(hour=17,minute=0,second=0)
        else:
            result = dt_start + timedelta(days=1)
            result = result.replace(hour=13,minute=0,second=0)

    elif description == "EOW":
        day_index = dt_start.weekday()
        if 0 <= day_index <= 2:
            result = dt_start + timedelta(days= 4 - day_index)
            result = result.replace(hour=17,minute=0,second=0)
        elif 3 <= day_index <= 4:
            result = dt_start + timedelta(days= 6 - day_index)
            result = result.replace(hour=20,minute=0,second=0)

    elif description[-1] == "M":
        target_month = int(description[:-1])
        target_year = dt_start.year

        if dt_start.month >= target_month:
            target_year += 1

        result = datetime(target_year, target_month, 1, 8, 0, 0)

        day_index = result.weekday()
        if 5 <= day_index <= 6:
            result += timedelta(days= 7 - day_index)

    elif description[0] == "Q":
        target_quarter = int(description[1])
        start_quarter = round(dt_start.month - 1 // 3)
        target_year = dt_start.year
        target_month = target_quarter * 3

        if start_quarter > target_quarter:
            target_year += 1

        result = datetime(target_year, target_month, calendar.monthrange(target_year, target_month)[1], 8, 0, 0)

        day_index = result.weekday()
        if 5 <= day_index <= 6:
            result -= timedelta(days= day_index - 4)

    if result:
        return result.isoformat()
    return None