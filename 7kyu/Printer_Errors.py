def printer_error(s):
    # your code
    base_lst = [chr(i) for i in list(range(ord('a'), ord('n')))]
    cnt = 0
    for i in s:
        if i not in base_lst:
            cnt += 1
    return str(cnt) + "/" + str(len(s))        