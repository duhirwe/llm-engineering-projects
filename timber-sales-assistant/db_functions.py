import sqlite3


DB = "timber.db"

def get_available_timber_types():
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
    cursor.execute("SELECT type, unit_price FROM timber_prices")
    rows = cursor.fetchall()

    if not rows:
        return "No timber types are currently available."

    result = "Available timber types:\n"
    for timber_type, unit_price in rows:
        result += f"- {timber_type}: {unit_price:,.0f} RWF per unit\n"

    return result



def get_timber_price(timber_type):
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()

    cursor.execute(
        "SELECT unit_price FROM timber_prices WHERE LOWER(type) = LOWER(?)",
        (timber_type,)
    )
    row = cursor.fetchone()

    if row:
        return f"The unit price of {timber_type} is {row[0]:,.0f} RWF."
    else:
        return f"Sorry, {timber_type} is not available."
    


def calculate_timber_cost(timber_type, quantity):
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()

    cursor.execute(
        "SELECT unit_price FROM timber_prices WHERE LOWER(type) = LOWER(?)",
        (timber_type,)
    )
    row = cursor.fetchone()

    if not row:
        return f"Sorry, {timber_type} is not available."

    unit_price = row[0]
    total_price = unit_price * quantity

    return (
        f"{quantity} units of {timber_type} cost "
        f"{total_price:,.0f} RWF "
        f"at {unit_price:,.0f} RWF per unit."
    )