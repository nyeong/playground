def do_something_with a
  a[1] = nil
end

array = [1, 2, 3]
do_something_with array
puts array.inspect


