defmodule LanguageList do
  def new() do
    []
  end

  def add(list, language) do
    [language | list]
  end

  def remove([_ | list]) do
    list
  end

  def first([first | _]) do
    first
  end

  def count(list) do
    Enum.count(list)
  end

  def excting_list?([]), do: false
  def exciting_list?(list) do
    Enum.any?(list, &(&1 == "Elixir"))
  end
end
