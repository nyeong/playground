defmodule Matrix do
  defstruct matrix: nil
  @type t() :: %Matrix{}

  @doc """
  Convert an `input` string, with rows separated by newlines and values
  separated by single spaces, into a `Matrix` struct.
  """
  @spec from_string(input :: String.t()) :: t()
  def from_string(input) do
    matrix = input
    |> String.split("\n")
    |> Enum.map(&parse_row/1)

    %__MODULE__{ matrix: matrix }
  end

  @spec parse_row(String.t()) :: [[integer()]]
  defp parse_row(row) do
    row
    |> String.trim()
    |> String.split(" ")
    |> Enum.map(&String.to_integer/1)
  end

  @doc """
  Write the `matrix` out as a string, with rows separated by newlines and
  values separated by single spaces.
  """
  @spec to_string(matrix :: t()) :: String.t()
  def to_string(matrix) do
    matrix.matrix
    |> Enum.map_join("\n", fn row -> Enum.join(row, " ") end) 
  end

  @doc """
  Given a `matrix`, return its rows as a list of lists of integers.
  """
  @spec rows(matrix :: t()) :: [[integer()]]
  def rows(matrix), do: matrix.matrix

  @doc """
  Given a `matrix` and `index`, return the row at `index`.
  """
  @spec row(matrix :: t(), index :: integer) :: list(integer)
  def row(matrix, index), do: matrix.matrix |> Enum.at(index - 1)

  @doc """
  Given a `matrix`, return its columns as a list of lists of integers.
  """
  @spec columns(matrix :: t()) :: list(list(integer))
  def columns(matrix) do
    matrix.matrix
    |> List.zip()
    |> Enum.map(&Tuple.to_list/1)
  end

  @doc """
  Given a `matrix` and `index`, return the column at `index`.
  """
  @spec column(matrix :: t(), index :: integer) :: list(integer)
  def column(matrix, index) do
    matrix.matrix
    |> Enum.map(fn row -> Enum.at(row, index - 1) end)
  end
end
