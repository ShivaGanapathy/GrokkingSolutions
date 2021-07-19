#O(n)
def length_of_longest_substring(string, k):
  lp = max_repeat_count = output = 0
  chars = {}
  for rp in range(len(string)):
    right_char = string[rp]
    if right_char not in chars:
      chars[right_char] = 0
    chars[right_char] +=1
    max_repeat_count = max(max_repeat_count, chars[right_char])

    if rp - lp + 1 - max_repeat_count > k:
      left_char = string[lp]
      chars[left_char] -=1
      lp +=1
    output = max(output, rp-lp+1)
  
  return output
