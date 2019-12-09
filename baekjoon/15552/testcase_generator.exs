#

t = 1_000_000

IO.puts(t)

for _ <- 0..t do
  a = :random.uniform(1000)
  b = :random.uniform(1000)
  IO.puts("#{a} #{b}")
  IO.puts(:standard_error, "#{a + b}")
end
