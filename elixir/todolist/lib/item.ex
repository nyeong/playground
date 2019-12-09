defmodule Todolist.Item do
  defstruct description: nil, done: false

  @spec new(binary, boolean) :: Todolist.Item.t()
  def new(description, done \\ false) do
    %Todolist.Item{description: description, done: done}
  end

  @spec done(Todolist.Item.t()) :: Todolist.Item.t()
  def done(item) do
    %{item | done: true}
  end

  @spec undone(Todolist.Item.t()) :: Todolist.Item.t()
  def undone(item) do
    %{item | done: false}
  end
end
