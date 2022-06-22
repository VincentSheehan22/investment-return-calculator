# Investment return calcualtor.

def invest(amount, annual, term, roi):
    """Calculate investment value based on initial amount, term and rate of return."""
    for year in range(term):
        amount = amount + annual
        amount = amount + (amount * roi)
        print(f"Year {year + 1}: €{amount}")
    return amount


print(invest(1350, 1800, 7, 0.07))
