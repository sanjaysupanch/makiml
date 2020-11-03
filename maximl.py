from collections import defaultdict

s = input()
	
n = len(s) 

total_diff_chars = 0
diff_chars = defaultdict(int)

for i in range(n):
	if diff_chars[s[i]]==0:
		diff_chars[s[i]]+=1
		total_diff_chars+=1

new_count = defaultdict(lambda: 0)
count = 0
start = 0
ans = n 


for j in range(n): 
	new_count[s[j]] += 1
	
	if new_count[s[j]] == 1: 
		count += 1
		
	if count == total_diff_chars: 
		while new_count[s[start]] > 1: 
			if new_count[s[start]] > 1: 
				new_count[s[start]] -= 1
				
			start += 1
			
		len_window = j - start + 1
		
		if ans > len_window: 
			ans = len_window 
print(ans)