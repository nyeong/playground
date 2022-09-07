defmodule BoutiqueInventory do
  def sort_by_price(inventory) do
    inventory |> Enum.sort_by(fn item -> item[:price] end)
  end

  def with_missing_price(inventory) do
    inventory |> Enum.filter(&(!&1[:price]))
  end

  def update_names(inventory, old_word, new_word) do
    inventory |> Enum.map(fn %{name: name} = elem ->
      new_name = String.replace(name, old_word, new_word)
      %{elem | name: new_name}
    end)
  end

  def increase_quantity(item, count) do
    quantity_by_size = item[:quantity_by_size] |> Map.new(fn {k, v} -> {k, v + count} end)
    %{item | quantity_by_size: quantity_by_size}
  end

  def total_quantity(item) do
    Enum.reduce(item[:quantity_by_size], 0, fn {_, val}, acc -> val + acc end)
  end
end
