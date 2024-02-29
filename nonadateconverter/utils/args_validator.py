def validate_args(year: int,
                  month: int,
                  day: int
                  ):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError('Invalid year or month or day type')
