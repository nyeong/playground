# 접근
# 하라는 대로 한다
def solution(bridge_length, weight, truck_weights):
    # [(weight, elpased)]
    on_bridge = []
    total_elpased = 0
    while truck_weights or on_bridge:
        on_bridge = [(w, e + 1) for (w, e) in on_bridge]
        while on_bridge and on_bridge[0][1] == bridge_length:
            on_bridge = on_bridge[1:]
        if is_bridge_available(on_bridge, truck_weights, bridge_length, weight):
            on_bridge.append((truck_weights[0], 0))
            truck_weights = truck_weights[1:]
        total_elpased += 1
    return total_elpased

def is_bridge_available(on_bridge, wait_trucks, bridge_length, bridge_weight):
    sumup = sum([w for (w, _) in on_bridge])
    if wait_trucks and sumup + wait_trucks[0] <= bridge_weight:
        if len(on_bridge) + 1 <= bridge_length:
            return True
    return False
    
    
        
        
