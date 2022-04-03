# 피보나치 n항을 구하는 O(log n) 해법
require "matrix"

module Fib
  def self.get_nth n, a = 0, b = 1
    m = Matrix[[1, 1], [1, 0]]
    (m ** n * Matrix[[1], [0]]).row(1)[0]
  end
end
