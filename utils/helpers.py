def load_earnings_report(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

