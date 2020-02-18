defmodule RnaTranscription do
  @doc """
  Transcribes a character list representing DNA nucleotides to RNA

  ## Examples

  iex> RnaTranscription.to_rna('ACTG')
  'UGAC'
  """
  @spec to_rna([char]) :: [char]
  def to_rna(rna) when is_list(rna) do
    rna |> Enum.map(&to_rna/1)
  end

  @doc """
  Transcribes a character representing DNA nucleotides to RNA

  ## Examples

  iex> RnaTranscription.to_rna(?A)
  ?U
  """
  @spec to_rna(char) :: char
  def to_rna(char) do
    case char do
      ?G -> ?C
      ?C -> ?G
      ?T -> ?A
      ?A -> ?U
    end
  end
end
