def solution(다리길이제한, 다리무게제한, truck_weights)
    다리트럭 = [] # (트럭무게, 출발한시간)
    대기트럭 = truck_weights.dup
    다리무게 = 0
    시간 = 0

    until 대기트럭.empty? and 다리트럭.empty? do
        unless 다리트럭.empty? or 시간 - 다리트럭.first[1] != 다리길이제한
            나간트럭, _ = 다리트럭.shift
            다리무게 -= 나간트럭
        end

        unless 대기트럭.empty? or 다리무게 + 대기트럭.first > 다리무게제한 or 다리트럭.size + 1 > 다리길이제한
            출발트럭 = 대기트럭.shift
            다리무게 += 출발트럭
            다리트럭 << [출발트럭, 시간]
        end

        시간 += 1
    end

    시간
end
