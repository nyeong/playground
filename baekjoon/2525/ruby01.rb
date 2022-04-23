h,m=gets.chomp.split.map(&:to_i)
c=gets.chomp.to_i

h += c / 60
m += c % 60

h += 1 and m -= 60 if m >= 60
h -= 24 if h >= 24

puts "#{h} #{m}"