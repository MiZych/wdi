a, b = 1, 1
for i in range(0, 100):
    if a < 1000000:
        print("F%d / F%d = %d / %d, %.10f" %(i+1, i, b, a, b/a))
        a, b = b, a + b
    else:
        break
