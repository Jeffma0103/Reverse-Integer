# Reverse-Integer (medium)
Solution of  Reverse Integer

## 題目 https://leetcode.com/problems/reverse-integer/description/

將 32 bit 的整數翻轉, 如果結果超出 [-2^31, 2^31 - 1] 的範圍, 則 return 0

**ex1:** <br> 

Input: <br> 
x = 123 <br>

Output: <br>
321

**ex2:** <br> 

Input: <br> 
x = -123 <br>

Output: <br>
-321

**ex3:** <br> 

Input: <br> 
x = 120 <br>

Output: <br>
21


## Workaround &nbsp; 1

**想法** <br> 

* 寫一個 check function 判斷結果值是否在範圍內
* 判斷 x 是否等於 0
* 判斷 x 為正負值
* 翻轉後的結果再由 check function 進行判斷
