
import csv

if __name__ == '__main__':

    found = ['list_20260101_1200.csv', 'list_20260121_1610.csv', 'list_20260122_1429.csv']

    yesterday = dict()

    with open(found[-2], newline='') as f:
        rdr = csv.reader(f)
        top = next(rdr)
        for row in rdr:
            key = f"{row[0]}_{row[1]}_{row[2]}"
            yesterday[key] = row

    today = dict()

    with open(found[-1], newline='') as f:
        rdr = csv.reader(f)
        top = next(rdr)
        for row in rdr:
            key = f"{row[0]}_{row[1]}_{row[2]}"
            today[key] = row

    print(f"yesterday # {len(yesterday)}")
    print(f"today # {len(today)}")

    diff = list(set(today.keys()) - set(yesterday.keys()))

    for d in diff:
        print(f"    diff: {today[d]}")

