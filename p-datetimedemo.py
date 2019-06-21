# from datetime import date, time
from datetime import datetime, timedelta


def main():
    # today = date.today()
    # print(today)
    currenttimeStamp = datetime.now()
    currenttime = datetime.time(datetime.now())
    currentdate = datetime.date(datetime.now())
    print("date : ", currentdate, "time : ", currenttime, "timestamp : ", currenttimeStamp)

    print(currenttimeStamp.strftime("%A %d %B, %Y"))

    print((currenttimeStamp + timedelta(days=-365)).strftime("%A %d %B, %Y"))


if __name__ == "__main__":
    main();
