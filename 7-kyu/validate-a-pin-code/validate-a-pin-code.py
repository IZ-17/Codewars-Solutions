def validate_pin(pin):
    return pin.isdigit() and (len(pin) in (4,6))