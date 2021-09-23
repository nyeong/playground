defmodule LogLevel do
  def to_label(level, legacy?) do
    case {level, legacy?} do
      {0, true} -> :unknown
      {0, _} -> :trace
      {1, _} -> :debug
      {2, _} -> :info
      {3, _} -> :warning
      {4, _} -> :error
      {5, true} -> :unknown
      {5, _} -> :fatal
      {_, _} -> :unknown
    end
  end

  def alert_recipient(level, legacy?) do
    label = to_label(level, legacy?)
    cond do
      Enum.member?([:error, :fatal], label) -> :ops
      label == :unknown && legacy? -> :dev1
      label == :unknown && not legacy? -> :dev2
      true -> nil
    end
  end
end
