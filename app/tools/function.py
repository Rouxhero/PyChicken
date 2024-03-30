def date_formarter(date: str) -> str:
    return datetime.datetime.strptime(date, "%d/%m/%Y, %H:%M PM").strftime(
        "%Y:%m:%d %H:%M:00"
    )