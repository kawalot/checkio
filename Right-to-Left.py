#You are given a sequence of strings. You should join these strings into chunk of text where the initial strings are separated by commas. 
#As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left", even if it's a part of another word. 
#All strings are given in lowercase.
#Input: A sequence of strings as a tuple of strings (unicode).
#Output: The text as a string.


def left_join(phrases):
	string = ""
	for word in phrases:
		string = string + "".join(word + ",")
	string = string[:-1].replace("right","left")
	return string

print(left_join(("left", "right", "left", "stop")))
print(left_join(("bright aright", "ok")))
print(left_join(("brightness wright",)))
print(left_join(("enough", "jokes")))