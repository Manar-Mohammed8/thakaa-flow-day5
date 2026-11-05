def to_minutes(time_text):
    parts = time_text.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])

    return hours * 60 + minutes


def daily_points(checkin, on_time, total_tasks, report_on_time, scores):
    if to_minutes(checkin) < 600:
        attendance = 5
    else:
        attendance = 0

    if total_tasks == 0:
        tasks = 0
        quality = 0
    else:
        tasks = 10 * on_time / total_tasks
        quality = 10 * (sum(scores) / (10 * total_tasks))

    if report_on_time:
        report = 5
    else:
        report = 0

    return attendance + tasks + report + quality


trainees = [
    {"name": "Sara", "checkin": "09:40", "on_time": 5, "report_on_time": False, "scores": [8, 8, 8, 8, 8]},
    {"name": "Omar", "checkin": "10:15", "on_time": 4, "report_on_time": True, "scores": [9, 9, 9, 9, 0]},
    {"name": "Lina", "checkin": "08:55", "on_time": 5, "report_on_time": True, "scores": [10, 9, 9, 10, 8]},
    {"name": "Manar", "checkin": "09:00", "on_time": 5, "report_on_time": True, "scores": [10, 10, 10, 10, 8]},
]
total_tasks = 5

for t in trainees:
    t["points"] = daily_points(t["checkin"], t["on_time"], total_tasks, t["report_on_time"], t["scores"])

total_points = 0
best = trainees[0]

for t in trainees:
    print(f"{t['name']}: {t['points']}")
    total_points = total_points + t["points"]
    if t["points"] > best["points"]:
        best = t

average = total_points / len(trainees)
print(f"Average: {average}")
print(f"Best of the Day: {best['name']}")

lina_points = trainees[2]["points"]
my_points = trainees[3]["points"]

print(my_points - lina_points)
# اخترت الحضور قبل الساعة 10 وانجاز جميع المهام وتسليم التقرير في الوقت المحدد.
# جعلت مجموع الدرجات 48 للحصول على جودة 9.6 فأصبحت نقاطي 29.6 مقابل 29.2 لـ Lina.
# اختبار يوم بلا مهام
print(daily_points("09:00", 0, 0, True, []))
# عند طباعة الفرق ظهر 0.3999999999999986 مو 0.4 بالضبط، بسبب تمثيل الأعداد العشرية في بايثون.