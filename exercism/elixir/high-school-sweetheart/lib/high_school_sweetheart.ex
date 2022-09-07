defmodule HighSchoolSweetheart do
  def first_letter(name) do
    name |> String.trim_leading |> String.at(0)
  end

  def initial(name) do
    first_letter(name) |> String.upcase() |> Kernel.<>(".")
  end

  def initials(full_name) do
    String.split(full_name, " ")
    |> Enum.map(&initial/1)
    |> Enum.join(" ")
  end

  def pair(full_name1, full_name2) do
    full1 = initials(full_name1)
    full2 = initials(full_name2)
    """
         ******       ******
       **      **   **      **
     **         ** **         **
    **            *            **
    **                         **
    **     #{full1}  +  #{full2}     **
     **                       **
       **                   **
         **               **
           **           **
             **       **
               **   **
                 ***
                  *
    """
  end
end
