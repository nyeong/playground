defmodule WordCount do
  @doc """
  Count the number of words in the sentence.

  Words are compared case-insensitively.

  ## Example
  ```
  > WordCount.count("word")
  %{"word" => 1}
  ```
  """
  @spec count(String.t()) :: map
  def count(sentence) do
    reducer = fn x, acc ->
      x = String.downcase(x)
      Map.update(acc, x, 1, &(&1 + 1))
    end

    sentence
      # u modifiers to enable Unicode!
      |> String.split(~r/(?!-)[[:space:][:punct:]]/u, trim: true)
      |> Enum.reduce(%{}, reducer)
  end
end
