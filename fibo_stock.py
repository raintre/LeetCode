def fibonacci(n):
	ans, ans_next = 0, 1
	for i in range(n):
		ans, ans_next = ans_next, ans + ans_next
	print(ans)
fibonacci(10)

# -> 55