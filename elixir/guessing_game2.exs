defmodule GuessingGame do
  def compare(answer, guess) do
    cond do
      answer < guess ->
        IO.puts("좀 커요")
        get_input(answer)

      answer > guess ->
        IO.puts("좀 작아요")
        get_input(answer)

      answer == guess ->
        IO.puts("참 잘했어요!")
    end
  end

  def get_input(answer) do
    input = IO.gets("숫자를 맞춰보세요!\n")

    case Integer.parse(input) do
      {guess, _} -> compare(answer, guess)
      :error -> get_input(answer)
    end
  end
end

answer = :rand.uniform(99)
IO.puts("정답은 #{answer} 입니다.")
GuessingGame.get_input(answer)
