# def voice_price(words, rate=10):
# 	return words * rate
#
#
# voice_price(100, 100)
# print(voice_price(100, 100))


#
#
# def voice_price(points, threshold=10):
#     if points >= threshold:
#         return True
#     else:
#         return False
#
#
# voice_price(12, 10)

def shift_point(point, dx, dy):
    my_list = list(point)
    my_list[0] += dx
    my_list[1] += dy
    return my_list


shift_point((1, 4), 2, 3)

print(my_list)
