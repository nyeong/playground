defmodule RomanNumerals do
  @roman_units [
    {1000, "M"},
    {900, "CM"},
    {500, "D"},
    {400, "CD"},
    {100, "C"},
    {90, "XC"},
    {50, "L"},
    {40, "XL"},
    {10, "X"},
    {9, "IX"},
    {5, "V"},
    {4, "IV"},
    {1, "I"},
  ]

  @doc """
  Convert the number to a roman number.

  ## Example

  ```
  iex> numeral(3) == "III"
  ```
  """
  @spec numeral(pos_integer) :: String.t()
  def numeral(number) do
    @roman_units
      |> Enum.reduce({number, ""}, &reducer/2)
      |> elem(1)
  end

  defp reducer({divider, roman}, {number, acc}) do
    if div(number, divider) > 0 do
      reducer({divider, roman}, {number - divider, acc <> roman})
    else
      {number, acc}
    end
  end
end
