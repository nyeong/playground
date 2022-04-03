defmodule Chop do
  def guess(actual, first..last) do
    middle = div(first + last, 2)
    IO.puts "It Is #{middle}"
    _guess(actual, first..last, middle)
  end

  defp _guess(actual, _, middle) when actual == middle, do: actual
  defp _guess(actual, _..last, middle) when actual > middle do
    guess(actual, middle..last)
  end
  defp _guess(actual, first.._, middle) when actual < middle do
    guess(actual, first..middle)
  end
end

