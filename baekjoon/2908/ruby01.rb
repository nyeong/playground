puts ($<.read.split(" ").map do |x|
  x.split("").reverse.join("")
end.max)
