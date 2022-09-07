tally = gets.chomp.downcase.split("").tally.sort_by(&:last)

if tally[-2] and tally[-1][1] == tally[-2][1]
  puts "?" 
else
  puts tally[-1][0].upcase
end
