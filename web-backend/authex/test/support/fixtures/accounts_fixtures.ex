defmodule Authex.AccountsFixtures do
  @moduledoc """
  This module defines test helpers for creating
  entities via the `Authex.Accounts` context.
  """

  @doc """
  Generate a user.
  """
  def user_fixture(attrs \\ %{}) do
    {:ok, user} =
      attrs
      |> Enum.into(%{
        name: "some name",
        password_hash: "some password_hash",
        username: "some username"
      })
      |> Authex.Accounts.create_user()

    user
  end
end
