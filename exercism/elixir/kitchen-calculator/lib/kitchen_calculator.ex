defmodule KitchenCalculator do
  @type unit :: :millimiter | :cup | :fluid_ounce | :teaspoon | :tablespoon
  @type ml :: {:millimiter, float()}
  @type cup :: {:cup, float()}
  @type fluid_ounce :: {:fluid_ounce, float()}
  @type teaspoon :: {:teaspoon, float()}
  @type tablespoon :: {:tablespoon, float()}

  def get_volume({_, volume}), do: volume

  @spec to_milliliter(ml | cup | fluid_ounce | teaspoon | tablespoon) :: ml
  def to_milliliter({:milliliter, content}), do: {:milliliter, content}
  def to_milliliter({:cup, content}), do: {:milliliter, content * 240}
  def to_milliliter({:fluid_ounce, content}), do: {:milliliter, content * 30}
  def to_milliliter({:teaspoon, content}), do: {:milliliter, content * 5}
  def to_milliliter({:tablespoon, content}), do: {:milliliter, content * 15}

  @spec from_milliliter(ml, unit) :: ml | cup | fluid_ounce | teaspoon | tablespoon
  def from_milliliter({:milliliter, content}, :milliliter), do: {:milliliter, content}
  def from_milliliter({:milliliter, content}, :cup), do: {:cup, content / 240.0}
  def from_milliliter({:milliliter, content}, :fluid_ounce), do: {:fluid_ounce, content / 30.0}
  def from_milliliter({:milliliter, content}, :teaspoon), do: {:teaspoon, content / 5.0}
  def from_milliliter({:milliliter, content}, :tablespoon), do: {:tablespoon, content / 15.0}

  @spec convert(ml | cup | fluid_ounce | teaspoon | tablespoon, unit) :: ml | cup | fluid_ounce | teaspoon | tablespoon
  def convert(volume_pair, unit) do
    volume_pair |> to_milliliter() |> from_milliliter(unit)
  end
end
