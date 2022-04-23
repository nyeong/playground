defmodule KitchenCalculator do
  @unit_table %{
      milliliter: 1,
      cup: 240,
      fluid_ounce: 30,
      teaspoon: 5,
      tablespoon: 15,
    }

  @doc """
      KitchenCalculator.get_volume({:cup, 2.0})
      # => 2.0
  """
  def get_volume({_, num}), do: num

  def to_milliliter({measure, num}) when is_map_key(@unit_table) do
    {:milliliter, num * Map.get(measure)}
  end

  def from_milliliter(volume_pair, unit) do
    # Please implement the from_milliliter/2 functions
  end

  def convert(volume_pair, unit) do
    # Please implement the convert/2 function
  end
end
