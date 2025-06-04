names_tuples= ("shardul","ravi","folyyy","25","10.2","kolr")
print(names_tuples)
# REMEMBERRRRRR
#TUPLES ARE IMMMUTABLE CANNOT CHANGE THE VALUE
#WRITE IN BRACKETS() PARENTHESIS.
#TO CHANGE THE VALUE IN TUPLES- FIRST CHANGE INTO LIST -> APPEND THE VALUE PRINT AND THEN REVERSE BACK TO TUPLE.

convert_tuple_to_list = list(names_tuples)
convert_tuple_to_list.sort()
print(convert_tuple_to_list)
reverse_back_to_tuple = tuple(convert_tuple_to_list)
print(reverse_back_to_tuple)