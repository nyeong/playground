defmodule Stack do
  use GenServer

  def init(stack) do
    {:ok, stack}
  end

  def handle_call(:pop, _from, [head | tail]) do
    {:reply, head, tail}
  end

  def handle_cast({:push, elem}, state) do
    {:noreply, [elem | state]}
  end

  def handle_call(:clean, _from, _state) do
    {:noreply, []}
  end

  def start_link(default) when is_list(default) do
    GenServer.start_link(__MODULE__, default)
  end

  def push(pid, element) do
    GenServer.cast(pid, {:push, element})
  end

  def pop(pid) do
    GenServer.call(pid, :pop)
  end
end
