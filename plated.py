def day_schedule(requests):
    cleaned = []
    for time in requests:
        mins = 0 if "am" in time else 720
        mins += (60 * int(time[:2] if time[:2] != "12" else 0)) + int(time[3:5])
        duration = int(time.split(",")[1])
        end = mins + duration
        if 480 <= mins <= 1080 and duration > 0 and 480 <= end <= 1080:
            end = 1080 if end >= 1075 else end + 5
            cleaned.append((mins - 480, end - 480, duration))
    print cleaned


day_schedule(["10:00am, 30", "10:15am, 45", "11:00am, 20", "11:15am, 60", "12:30pm, 60", "01:00pm, 75"])
