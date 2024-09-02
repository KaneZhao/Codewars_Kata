def pyramid(stones):
    dic = {}
    for i in stones:
        dic[i] = dic.get(i, 0) + 1
    nums = [(k, v) for k,v in dic.items()]
    nums.sort(key=lambda i: (i[0]), reverse=True)
    num1, num2, num3 = None, None, None
    if len(nums) < 3:
        return None
    for i in nums:
        if num3 is None:
            if i[1] >= 3:
                num3 = i[0]
            elif i[1] >= 2 and num2 is None:
                num2 = i[0]
            elif i[1] >= 1 and num1 is None:
                num1 = i[0]
        else:
            if num2 is None:
                if i[1] >= 2:
                    num2 = i[0]
                elif i[1] >= 1 and num1 is None:
                    num1 = i[0]
            else:
                if num1 is None:
                    num1 = i[0]
                else:
                    return num1 + num2 * 2 + num3 * 3
    return num1 + num2 * 2 + num3 * 3 if (num1 and num2 and num3) else None 