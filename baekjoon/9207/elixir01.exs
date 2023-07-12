defmodule Solve do
  def get

  def main do
    IO.gets("")
  end
end

IO.gets("")
|> String.trim()
|> String.to_integer()
|> (&(1..&1)).()
|> Enum.each(fn _ -> Solve.main() end)
