# def romanToInt(s):
#     value_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
#     output = value_dict[s[0]]
#     for i in range(1, len(s)):
#         if value_dict[s[i-1]] < value_dict[s[i]]:
#             output += value_dict[s[i]] - value_dict[s[i-1]] - value_dict[s[i-1]]
#         else:
#             output += value_dict[s[i]]
#     return output

# print(romanToInt("MCMXCIV"))

nums = [1,2,2,1]

def removeElement(nums, val):
    output = []
    lastval = []
    for n in nums:
        if n!=val: output.append(n)
        else: lastval.append("_")
    return(output+lastval)

print(removeElement(nums, 1))