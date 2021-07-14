def non_repeat_substring(string):
  lp = 0
  chars = {}
  output = 0
  
  for rp in range(len(string)):
    right_char = string[rp]
    if right_char in chars:
      lp = max(lp, chars[right_char]+1)
    chars[right_char] = rp

    output = max(output,rp-lp+1)
  return output
      
  
  
