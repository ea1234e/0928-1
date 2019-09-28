def getMean(numericValue):
    return sum(numericValue)/len(numericValue)

my_list2 = [1, 2, 3]

try:
    result = getMean(my_list2)
except ZeroDivisionError as detail:
    print("(Error): {}".format(float('nan')))
    print("(Error): {}".format(detail))
else:
    print("(The mean is): {}".format(result))
finally:
    print("(Finally): The Finally block is executed every time")

