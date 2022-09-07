lines = $<.readlines[1..].map(&:chomp)

scores = lines.map do |line|
  line.split("").inject(acc: 1, sum: 0) do |m, x|
    next {sum: m[:sum], acc: 1} if x == "X"
    {sum: m[:acc] + m[:sum], acc: m[:acc] + 1}
  end[:sum]
end

puts scores
