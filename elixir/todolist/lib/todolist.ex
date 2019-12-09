defmodule Todolist do
  @doc """
  Creates new todolist.

      iex> Todolist.start_link
  """
  def start_link do
    Agent.start_link(fn -> [] end)
  end

  def
end
