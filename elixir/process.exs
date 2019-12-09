defmodule TrackingState do
  def loop(state \\ []) do
    receive do
      {:push, item} -> state = [item | state]
      whatever -> {:error, "#{whatever} is not a valid"}
    end
    IO.inspect(state)
    loop(state)
  end
end
