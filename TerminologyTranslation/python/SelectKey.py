def SelectKey(i, subject):
    if i % 6 == 0:
        return "{japanese:\""
    elif i % 6 == 1:
        return "\",kana:\""
    elif i % 6 == 2:
        return "\",roman:\""
    elif i % 6 == 3:
        return "\",translation:\""
    elif i % 6 == 4:
        return "\",meaning:\""
    else:
        return "\",subject:\"" + subject + "\"}"
