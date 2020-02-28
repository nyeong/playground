defmodule SecretHandshake do
  @secrets [
    {0b1000, "jump"},
    {0b0100, "close your eyes"},
    {0b0010, "double blink"},
    {0b0001, "wink"},
  ]
  use Bitwise

  @doc """
  Determine the actions of a secret handshake based on the binary
  representation of the given `code`.

  If the following bits are set, include the corresponding action in your list
  of commands, in order from lowest to highest.

  1 = wink
  10 = double blink
  100 = close your eyes
  1000 = jump

  10000 = Reverse the order of the operations in the secret handshake
  """
  @spec commands(code :: integer) :: list(String.t())
  def commands(code) do
    coded = @secrets |> Enum.reduce([], fn {key, value}, acc ->
      if (key &&& code) !== 0,
        do: [value | acc],
        else: acc
    end)

    if (code &&& 0b10000) !== 0, do: Enum.reverse(coded), else: coded
  end
end
