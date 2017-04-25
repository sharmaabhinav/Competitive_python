noOfDays, K = map(int, raw_input().split(" "))
costs = map(int, raw_input().split(" "))
sorted_costs = sorted(costs)[::-1]


possible_visits = noOfDays / K + 1

start = 1
split_index_start = 0
split_index_last = split_index_start + K
optimalCost = 0
while(start <= possible_visits):
  optimalCost += sum(sorted_costs[split_index_start: split_index_last]) * start
  split_index_start += K
  split_index_last = split_index_start + K
  start += 1

print optimalCost
