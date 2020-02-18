defmodule WordCount do
  @doc """
  Count the number of words in the sentence.

  Words are compared case-insensitively.
  """
  @spec count(String.t()) :: map
  def count(sentence) do
    reducer = fn x, acc ->
      x = String.downcase(x)
      Map.update(acc, x, 1, &(&1 + 1))
    end

    sentence
      |> String.replace(~r/[!:,@#$%^&]/, "")
      |> String.split(~r/(\s|_)/, trim: true)
      |> Enum.reduce(%{}, reducer)
  end
end
