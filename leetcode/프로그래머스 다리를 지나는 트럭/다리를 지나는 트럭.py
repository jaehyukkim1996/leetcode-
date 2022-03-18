def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length

    counter = 0
    while True:
        if truck_weights:
            truck = truck_weights.pop(0)
            bridge.pop()

            if sum(bridge) + truck <= weight:
                bridge.insert(0, truck)
            else:
                bridge.insert(0, 0)
                truck_weights.insert(0, truck)
        else:
            bridge.pop()
            bridge.insert(0, 0)

        counter += 1
        # print truck_weights, bridge

        if sum(truck_weights) == 0:
            return counter + bridge_length



print(solution(2, 10, [7,4,5,6]))