defmodule MakeStar do
  require Integer

  def print(n) do
    1..height(n) |> Enum.map(&get_line(n, &1))
                 |> Enum.each(fn str -> IO.puts(str) end)
  end

  def height(n), do: 4 * n - 3

  def get_line(n, line) when Integer.is_odd(line) do
    leftnum = div(line - 1, 2) |> make_lower_then(n - 1)
    halfhalf("* ", "**", leftnum, n - 1 - leftnum)
    <> "*"
    <> halfhalf("**", " *", n - 1 - leftnum, leftnum)
  end


  def get_line(n, line) when Integer.is_even(line) do
    leftnum = div(line, 2) |> make_lower_then(n - 1, 1)
    halfhalf("* ", "  ", leftnum, n - 1 - leftnum)
    <> " "
    <> halfhalf("  ", " *", n - 1 - leftnum, leftnum)
  end

  def make_lower_then(num, standard, plus \\ 0) do
    if num <= standard do
      num
    else
      2 * trunc(standard) - num + plus
    end
  end

  def halfhalf(patternA, patternB, numA, numB), do:
    String.duplicate(patternA, numA) <> String.duplicate(patternB, numB)
end

{n, _} = IO.gets("") |> Integer.parse()

MakeStar.print(n)
