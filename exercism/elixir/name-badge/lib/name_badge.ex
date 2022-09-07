defmodule NameBadge do
  def print(nil, name, department) do
    department = if department, do: department, else: "OWNER"
    department = String.upcase(department)
    "#{name} - #{department}"
  end

  def print(id, name, department) do
    "[#{id}] - " <> print(nil, name, department)
  end
end
