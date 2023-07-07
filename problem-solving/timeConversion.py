def timeConversion(s):
    am_pm = s[-2:]
    str_split = s[:-2].split(':')

    h = int(str_split[0])

    if h == 12 and am_pm == "AM":
        str_split[0] = "00"
    elif h == 12 and am_pm == "PM":
        str_split[0] = "12"
    elif am_pm == "PM":
        str_split[0] = str(h + 12)
    else:
        str_split[0]

    return(':'.join(str_split))
