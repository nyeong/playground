map=[0,0,0].map{gets.to_i}.reduce(&:*).to_s.split("").tally
("0".."9").each{|x|puts map[x]?map[x]:0}
