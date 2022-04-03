# O(n) 해법

# 두 개의 초항이 주어졌을 경우의 피보나치 수열
# Endless Enumerator로 반환한다.
def fib(a, b)
  Enumerator.new do |y|
    loop do
      y << a
      a, b = b, a + b
    end
  end
end

puts fib(1, 2)
  .lazy
  .take_while { |x| x < 4_000_000 }
  .filter(&:even?)
  .sum
