#O(n) Sliding Windows
def smallest_subarray_with_given_sum(s, arr):
  import math
  lp = rp = 0
  curSum = 0
  output = math.inf
  while rp != len(arr):
    curSum += arr[rp]
    while curSum >= s:
      output = min(output, rp-lp+1)
      curSum -= arr[lp]
      lp +=1
    rp+=1
      
  return output
