import networkx as nx


class CriticalPath:
    def __init__(self, activities):
        activities['start'] = 0
        activities['end'] = 0
        self.activities = activities

    def calculate_critical_path(self):
        dependencies = {
            '1': ['start'],
            '2': ['1'],
            '3': ['2'],
            '4': ['3'],
            '5': ['4'],
            '6': ['5'],
            '7': ['6'],
            '8': ['6'],
            '9': ['7'],
            '10': ['7'],
            '11': ['8'],
            '12': ['8', '10'],
            '13': ['11'],
            '14': ['19'],
            '15': ['7'],
            '16': ['15'],
            '17': ['7'],
            '18': ['7'],
            '19': ['7'],
            '20': ['12', '13', '14', '16','17','18'],
            'end': ['20']
        }

        # ایجاد یک گراف جهت‌دار
        G = nx.DiGraph()
        activities = self.activities
        # اضافه کردن گره‌ها به گراف با وزن برابر با زمان اجرای فعالیت
        for activity, duration in activities.items():
            G.add_node(activity, duration=duration)

        # اضافه کردن یال‌ها بر اساس پیش‌نیازها
        for activity, prereqs in dependencies.items():
            for prereq in prereqs:
                # افزودن یک یال از پیش‌نیاز به فعالیت با وزن برابر با زمان اجرای پیش‌نیاز
                G.add_edge(prereq, activity, weight=activities[prereq])

        # محاسبه مسیر بحرانی با استفاده از طولانی‌ترین مسیر
        critical_path = nx.dag_longest_path(G)
        critical_path_duration = nx.dag_longest_path_length(G)

        return critical_path_duration

# activities = {
#     '1': 13,
#     '2': 67,
#     '3': 4,
#     '4': 22,
#     '5': 18,
#     '6': 224,
#     '7': 111,
#     '8': 58,
#     '9': 53,
#     '10': 91,
#     '11': 93,
#     '12': 104,
#     '13': 98,
#     '14': 127,
#     '15': 20,
#     '16': 40,
#     '17': 40,
#     '18': 216,
#     '19': 287,
#     '20': 13,
# }
# cp = CriticalPath(activities)
# total_duration, critical_path = cp.calculate_critical_path()
# print(critical_path)
# print(total_duration)
