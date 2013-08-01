'''
Calculate if one sequence is subsequence of another one
e.g. [3, 3, 4, 5] is an subsequence of [3, 4, 3, 5, 4, 3, 5]
'''
def is_subsequence(seq1, seq2):
  if seq1 is None or seq2 is None:
    return False
  if not seq1 or seq1 == seq2:
    return True
  ind = 0
  for i in range(len(seq2)):
    if seq2[i] == seq1[ind]:
      ind += 1
      if ind >= len(seq1):
        return True
  return False

def test_is_subsequence():
	if is_subsequence(None, None):
		raise Exception
	if not is_subsequence([], [3, 2, 3, 1]):
		raise Exception
	if not is_subsequence([3, 3, 2, 1], [1, 2, 3, 2, 3, 1, 2, 3, 1]):
		raise Exception
	if is_subsequence([3, 3, 2, 1], [3, 3, 1, 2, 2, 3, 3]):
		raise Exception

if __name__ == '__main__':
	test_is_subsequence()
