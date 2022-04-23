puts case ns=gets.split.map(&:to_i)
in [a, ^a, ^a]
  10_000 + a * 1_000
in [a, ^a, _]
  1_000 + a * 100
in [a, _, ^a]
  1_000 + a * 100
in [_, a, ^a]
  1_000 + a * 100
else
  ns.max * 100
end