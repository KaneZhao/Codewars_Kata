from preloaded import Like, Dislike, Nothing

def like_or_dislike(lst):
    res = Nothing
    for i in lst:
        if res == Nothing:
            res = i
        else:
            if res == i:
                res = Nothing
            else:
                res = i
    return res