#O(N*K) Brute Force
def max_sub_array_of_size_k(k, arr):
  output = 0
  for i in range(len(arr)-k+1):
    curSum = 0
    for j in range(i,i+k):
      curSum += arr[j]
    output = max(output,curSum)

  return output

#O(N) Sliding Windows
def max_sub_array_of_size_k(k, arr):
  lp = rp = 0
  curSum = 0
  output = 0
  while rp != len(arr):
    curSum += arr[rp]
    if rp-lp==k-1:
      if curSum>output:
        output = curSum
      curSum -= arr[lp]
      lp +=1
    rp +=1

