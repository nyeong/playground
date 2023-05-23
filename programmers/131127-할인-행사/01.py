from collections import Counter

def solution(want, number, discount):
    wants = dict(zip(want, number))
    amount = sum(number)
    day_count = 0
    
    # discounted[i] = i번째 날부터 amount일동안 살 수 있는 물건의 dict
    discounted = [Counter(discount[0:amount])]
    
    for i, product in enumerate(discount[0:-amount]):
        curr = discounted[-1].copy()
        curr[product] -= 1
        curr[discount[amount + i]] = curr.get(discount[amount + i], 0) + 1
        discounted.append(curr)
    
    for day in discounted:
        if is_dict_equal(day, wants):
            day_count += 1
            
    return day_count

def is_dict_equal(day, wants):
    for k in wants.keys():
        if not day[k] or day[k] != wants[k]:
            return False
    return True
