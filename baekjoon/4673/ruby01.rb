LIMIT = 9999

selfnums = [false] + [true] * LIMIT

def d n
  n.to_s.split("").map(&:to_i).sum() + n
end

(1..9980).each do |n|
  current_n = n
  current_dn = d n
  selfnums[current_dn] = false if current_dn <= LIMIT
end

selfnums.each_with_index do |x, i|
  puts i if x
end
