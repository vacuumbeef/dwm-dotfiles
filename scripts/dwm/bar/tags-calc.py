#!/usr/bin/env python
import sys, re
scan = None
ocpd = None

def extract(str):
	return int(re.findall(r'\d+', str)[0])

'''
def addf(arr, num):
	if num in arr:
		return " ".join(str(x) for x in arr).replace(str(num), 'F' + str(num))
	else:
		return " ".join(str(x) for x in sorted(arr + [num])).replace(str(num), 'F' + str(num))
'''

def stringify(arr):
    return " ".join(str(x) for x in arr)

def replace_element(lst, old_value, new_value):   # thx ChatGPT
    try:
        index = lst.index(old_value)
        lst[index] = new_value
        return lst
    except ValueError:
        print(f"{old_value} not found in the list.")

def addf (arr, num):
    if num in arr:
        return replace_element(arr, num, f"F{num}")
    else:
        return replace_element(sorted(arr + [num]), num, f"F{num}")

'''
def dumbhack(string):
    if "F1F1" in string:
        return string.replace("F1F1", "F11")
    else:
        return string
'''

def tags(num, power = 16, arr = []):
  if power >= 0:
    if num >= pow(2, power):
      return tags(num - pow(2, power), power - 1, arr + [power + 1])
    else:
      return tags(num, power - 1, arr)
  return arr[::-1]

for line in sys.stdin:
	if 'old_state' in line:
		scan = False
	if 'new_state' in line:
		scan = True
	if 'occupied' in line and scan:
		print(stringify(addf(tags(extract(line)), ocpd)))
	if 'selected' in line and scan:
		ocpd = tags(extract(line))[0]
