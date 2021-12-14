import requests

def linear_search(arr, x):
    result = []
    for i in arr:
        if int(i["h_in"]) == x:
            result.append(f"{i['first_name']} {i['last_name']}")
    return result

def print_pairs(result):
    if len(result) == 0:
        print("No matches found")
    pair = ""
    for i in range(len(result)):
        if (i+1) % 2 == 0:
            print(f"-{pair}\t{result[i]}\n")
            pair = ""
        else:
            pair += result[i]
    print(pair)

if __name__ == "__main__":
    r = requests.get("https://mach-eight.uc.r.appspot.com/").json()
    value_search = int(input("app: "))
    print_pairs(linear_search(r["values"], value_search))