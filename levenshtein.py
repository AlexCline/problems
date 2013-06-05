def levenshtein(string1, string2):
	s1, s2 = len(string1), len(string2)

	if s1 == 0:
		return s1
	if s2 == 0:
		return s2

	if (string1[s1 - 1] == string2[s2 - 1]):
		cost = 0
	else:
		cost = 1

	return min(levenshtein(string1[0:s1-1], string2) + 1,
			   levenshtein(string1, string2[0:s2-1]) + 1,
			   levenshtein(string1[0:s1-1], string2[0:s2-1]) + cost)


print levenshtein("dog", "cat")