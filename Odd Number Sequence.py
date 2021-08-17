_foundby_ = "zabilsabri"

n = 9 # YOUR ODD NUMBER INPUT
answer = 1

if n % 2 == 0: # CHECK IF YOUR INPUT NUMBER ODD OR EVEN
    print("ODD")
else:
    for i in range(n):
        if i % 2 != 0: # OMIT ALL EVEN NUMBER
            answer = answer + i
            answer += 2 # ADD 2 EVERY LOOPING

print(answer)