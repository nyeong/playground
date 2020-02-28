defmodule RotationalCipher do
  defguardp is_upcase(char) when ?A <= char and char <= ?Z
  defguardp is_downcase(char) when ?a <= char and char <= ?z
  defguardp is_alphabetic(char) when is_upcase(char) or is_downcase(char)

  @doc """
  Given a plaintext and amount to shift by, return a rotated string.

  Example:
  iex> RotationalCipher.rotate("Attack at dawn", 13)
  "Nggnpx ng qnja"
  """
  @spec rotate(text :: String.t(), shift :: integer) :: String.t()
  def rotate(text, shift) when is_binary(text) do
    text
      |> to_charlist()
      |> Enum.map(&(rotate(&1, shift)))
      |> to_string()
  end

  def rotate(char, shift) when is_alphabetic(char) do
    rotated = char + shift
    z = if is_upcase(char), do: ?Z, else: ?z
    cond do
      z < rotated -> rotated - 26
      true -> rotated
    end
  end

  def rotate(char, _shift), do: char
end
