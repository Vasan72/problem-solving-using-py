
def print_full_name(first, last):
    if len(first) <= 10 and len(last) <= 10:
        result = print(f"Hello {first} {last}! You just delved into python.")
        return result

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
