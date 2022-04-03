defmodule FizzBuzz do
  def fizzbuzz(0, 0, _), do: "FizzBuzz"
  def fizzbuzz(0, _, _), do: "Fizz"
  def fizzbuzz(_, 0, _), do: "Buzz"
  def fizzbuzz(_, _, c), do: c

  def fizzbuzz(n) do
    fizzbuzz(rem(n, 3), rem(n, 5), n)
  end
end
