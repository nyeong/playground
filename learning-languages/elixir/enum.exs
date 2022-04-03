defmodule MyEnum do
  def flatten(list) when is_list(list), do: _flatten(list, []) |> Enum.reverse
  defp _flatten([], result_list), do: result_list

  # when h is a list
  defp _flatten([h | t], result_list) when is_list(h) do
    _flatten(t, _flatten(h, []) ++ result_list)
  end

  # when h is not a list
  defp _flatten([h | t], result_list) do
    _flatten(t, [h | result_list])
  end
end
