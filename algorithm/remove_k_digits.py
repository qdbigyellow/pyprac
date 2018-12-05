



def remove_k_digits(s, k):
    new_s = s
    for k in range(len(s)):
        if int(s[k]) > int(s[k+1]):
            print(k)
            new_s = new_s[0:k] + new_s[k+1:]
            print(new_s)
            break

    return new_s

if __name__ == "__main__":
    remove_k_digits('45321', 1)
    