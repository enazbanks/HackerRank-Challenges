def timeConversion(s):
    am_pm = s[-2:]
    str_split = s[:-2].split(':')

    h = int(str_split[0])

    if h != 12 and am_pm == "PM":
        h += 12
    elif h == 12 and am_pm == "AM":
        h = 0

    str_split[0] = str(h).zfill(2)
    return(':'.join(str_split))

print(timeConversion("06:00:00AM"))
