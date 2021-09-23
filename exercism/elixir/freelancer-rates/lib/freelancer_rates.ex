defmodule FreelancerRates do
  @daily_rate_factor 8.0
  @month_rate_factor 22.0

  def daily_rate(hourly_rate) do
    hourly_rate * @daily_rate_factor
  end

  def apply_discount(before_discount, discount) do
    before_discount * (1 - discount / 100)
  end

  def monthly_rate(hourly_rate, discount) do
    hourly_rate
      |> daily_rate
      |> (&(&1 * @month_rate_factor)).()
      |> apply_discount(discount)
      |> ceil
  end

  def days_in_budget(budget, hourly_rate, discount) do
    expect_rate = daily_rate(hourly_rate) |> apply_discount(discount)
    budget / expect_rate
      |> Float.floor(1)
  end
end
