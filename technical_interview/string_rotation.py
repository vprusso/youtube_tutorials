# String Rotation: Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
# call to isSubstring (e.g. "waterbottle" is a rotation of "erbottlewat")

test_rot_str_1 = "waterbottle"
test_rot_str_2 = "erbottlewat"

test_rot_str_3 = "waterbottle"
test_rot_str_4 = "erbottlewat"
 
def is_string_rotation(str_1, str_2):

	alphabet = "abcdefghijklmnopqrstuvwxyz"
	if len(str_1) != len(str_2):
		return False

	str_1 = str_1.lower()
	str_2 = str_2.lower()

	dict_1 = dict.fromkeys(list(alphabet), 0)
	dict_2 = dict.fromkeys(list(alphabet), 0)

	for i in range(len(str_1)):
		dict_1[str_1[i]] += 1
		dict_2[str_2[i]] += 1

	return dict_1 == dict_2

print(is_string_rotation(test_rot_str_1, test_rot_str_2))
print(is_string_rotation(test_rot_str_3, test_rot_str_4))