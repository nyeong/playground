defmodule Secrets do
  use Bitwise

  def secret_add(secret) do
    fn number -> number + secret end
  end

  def secret_subtract(secret) do
    fn number -> number - secret end
  end

  def secret_multiply(secret) do
    fn number -> number * secret end
  end

  def secret_divide(secret) do
    fn number -> div number, secret end
  end

  def secret_and(secret) do
    fn number -> number &&& secret end
  end

  def secret_xor(secret) do
    fn number -> bxor number, secret end
  end

  def secret_combine(secret_function1, secret_function2) do
    fn number -> number |> secret_function1.() |> secret_function2.() end
  end
end
