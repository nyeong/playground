defmodule CaptainsLog do
  @planetary_classes ["D", "H", "J", "K", "L", "M", "N", "R", "T", "Y"]

  def random_planet_class() do
    @planetary_classes |> Enum.random()
  end

  def random_ship_registry_number() do
    number = Enum.random(1000..9999) |> to_string()
    "NCC-" <> number
  end

  def random_stardate() do
    41000.0 + :rand.uniform() * 1000
  end

  def format_stardate(stardate) when is_float(stardate) do
    :io_lib.format("~.1f", [stardate]) |> to_string
  end
  
  def format_stardate(_) do
    raise ArgumentError, message: "format_stardate must take float"
  end
end
