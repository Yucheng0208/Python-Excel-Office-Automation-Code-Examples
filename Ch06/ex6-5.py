def bill(minutes):
    if minutes <= 5 * 60:
        return minutes * 0.5
    else:
        return 5 * 60 * 0.5 + (minutes - 5 * 60) * 1

print(bill(300))
print(bill(400))