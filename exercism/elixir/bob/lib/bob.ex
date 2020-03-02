defmodule Bob do
  def hey(input) do
    case {
      question?(input),
      yell?(input),
      empty?(input),
    } do
      {_, _, true} -> "Fine. Be that way!"
      {true, true, _} -> "Calm down, I know what I'm doing!"
      {true, _, _} -> "Sure."
      {_, true, _} -> "Whoa, chill out!"
      _ -> "Whatever."
    end
  end

  defp question?(input) do
    String.trim_trailing(input) |> String.ends_with?("?")
  end

  defp yell?(input) do
    Regex.scan(~r/[[:lower:]]/, input) |> Enum.empty? and
    !(Regex.scan(~r/[[:upper:]]/, input) |> Enum.empty?)
  end

  defp empty?(input), do: String.trim(input) === ""
end
