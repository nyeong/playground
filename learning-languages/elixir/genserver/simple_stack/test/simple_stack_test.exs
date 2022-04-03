defmodule SimpleStackTest do
  use ExUnit.Case
  doctest SimpleStack

  test "simple stack basic works" do
    {:ok, stack} = SimpleStack.start_link()

    assert nil == SimpleStack.pop(stack)

    for i <- 1..10 do
      SimpleStack.push(stack, i)
    end

    for i <- 10..1 do
      assert i == SimpleStack.pop(stack)
    end
  end

end
