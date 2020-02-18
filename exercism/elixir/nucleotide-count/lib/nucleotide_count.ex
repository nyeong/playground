defmodule NucleotideCount do
  @nucleotides [?A, ?C, ?G, ?T]

  @doc """
  Counts individual nucleotides in a DNA strand.

  ## Examples

  iex> NucleotideCount.count('AATAA', ?A)
  4

  iex> NucleotideCount.count('AATAA', ?T)
  1
  """
  @spec count(charlist(), char()) :: non_neg_integer()
  def count(strand, nucleotide) do
    unless Enum.member?(@nucleotides, nucleotide) do
      raise ArgumentError, message: "#{nucleotide} is not a nucleotide"
    end

    Enum.count(strand, &(&1 == nucleotide))
  end

  @doc """
  Returns a summary of counts by nucleotide.

  ## Examples

  iex> NucleotideCount.histogram('AATAA')
  %{?A => 4, ?T => 1, ?C => 0, ?G => 0}
  """
  @spec histogram(charlist()) :: map()
  def histogram(strand) do
    init_map = %{
      ?A => 0,
      ?T => 0,
      ?C => 0,
      ?G => 0,
    }
    reducer = fn x, acc ->
      Map.update(acc, x, 0, &(&1 + 1))
    end

    Enum.reduce(strand, init_map, reducer)
  end
end
