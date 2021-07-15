#O(N) time complexity, O(K) Space Complexity
def longest_substring_with_k_distinct(String, k):
  lp = rp = 0
  chars = {}
  output = 0

  for rp in range(len(String)):
    
    #We add our right pointer's character to the hashmap each iteration
    if String[rp] not in chars:
      chars[String[rp]] = 0
    chars[String[rp]] += 1
    
    #If the length of our sliding window is over k, we use a while loop to get the lp at a good spot
    while len(chars.keys())>k:
      chars[String[lp]] -= 1
      if chars[String[lp]] == 0:
        del chars[String[lp]]
      lp +=1
    output = max(output,rp-lp+1)
      
  return output
