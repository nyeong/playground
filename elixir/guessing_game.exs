defmodule GuessingGame do
  def main() do
    IO.puts("Guess the number!")
    answer = :rand.uniform(100)
    IO.puts("the answer is #{answer}")
    do_get_input(answer)
  end

  defp do_get_input(answer) do
    input = IO.gets("Please input your guess: ") |> String.trim()

    case Integer.parse(input) do
      :error ->
        IO.puts("You typed wrong! Please type number only!")
        do_get_input(answer)

      {num, _} ->
        compare_number(num, answer)
    end
  end

  defp compare_number(input, answer) do
    cond do
      input > answer ->
        IO.puts("Too big!!")
        do_get_input(answer)

      input < answer ->
        IO.puts("Too small!!")
        do_get_input(answer)

      input === answer ->
        IO.puts("You're the best!")
    end
  end
end

GuessingGame.main()
