import datetime


# x = time.strptime(Arr[0].split(',')[0], '%H:%M:%S')
#     print(datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds())
def solution(S):
    calls_dict = {}
    for call in S.splitlines():
        number = call.split(',')[1]
        time = call.split(',')[0].split(':')
        time = int(time[0]) * 60 * 60 + int(time[1]) * 60 + int(time[2])
        if calls_dict.get(number):
            calls_dict[number] = calls_dict[number] + time
        else:
            calls_dict[number] = time
    max_seconds = max(calls_dict.values())
    free_number = min([num for num, sec in calls_dict.items() if sec == max_seconds])
    result = 0
    for num, sec in calls_dict.items():
        if num != free_number:
            if sec < 300:
                result += sec * 3
            else:
                i = 0
                if sec % 60 != 0:
                    i = 1
                result += (sec // 60 + i) * 150
    return result


def main():
    S = "00:05:00,701-080-080\n" \
        "00:01:07,400-234-092\n" \
        "0:05:00,400-234-092"
    print(solution(S))


if (__name__ == "__main__"):
    main()
