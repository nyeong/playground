defmodule SimpleStack do
  @moduledoc """
  A Stack implemented using GenServer
  """

  use GenServer

  # Client
  def start_link(default \\ []) when is_list(default) do
    GenServer.start_link(__MODULE__, default, name: __MODULE__)
  end

  @doc """
  Push an item to the stack.

  ## Example

    iex> {:ok, stack} = SimpleStack.start_link()
    iex> SimpleStack.push(stack, 1)
  """
  def push(elem) do
    GenServer.cast(__MODULE__, {:push, elem})
  end

  @doc """
  Pops an item from top of the stack.

  ## Example

    iex> {:ok, stack} = SimpleStack.start_link()
    iex> SimpleStack.pop(stack)
    nil
  """
  def pop() do
    GenServer.call(__MODULE__, :pop)
  end

  # Server
  def init(default) do
    {:ok, default}
  end

  def handle_cast({:push, elem}, list) do
    {:noreply, [elem | list]}
  end

  def handle_call(:pop, _from, []) do
    {:reply, nil, []}
  end

  def handle_call(:pop, _from, [head | tail]) do
    {:reply, head, tail}
  end

end
