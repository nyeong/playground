defmodule Authex.Accounts do
  @moduledoc """
  The Accounts context.
  """

  @jwk JOSE.JWK.generate_key({:oct, 16})

  import(Ecto.Query, warn: false)
  alias Authex.Repo
  alias Authex.Accounts.User
  alias JOSE.JWT

  @doc """
  Returns the list of users.

  ## Examples

      iex> list_users()
      [%User{}, ...]

  """
  def list_users do
    Repo.all(User)
  end

  @doc """
  Gets a single user.

  Raises `Ecto.NoResultsError` if the User does not exist.

  ## Examples

      iex> get_user!(123)
      %User{}

      iex> get_user!(456)
      ** (Ecto.NoResultsError)

  """
  def get_user!(id), do: Repo.get!(User, id)

  def get_user_by(attrs) when is_list(attrs), do: Repo.get_by(User, attrs)

  def verify_user_password(username, password) do
    user = get_user_by(username: username)

    cond do
      user && Pbkdf2.verify_pass(password, user.password_hash) ->
        {:ok, user}

      user ->
        {:error, :not_authorized}

      true ->
        Pbkdf2.no_user_verify()
        {:error, :not_found}
    end
  end

  def issue_token(%User{username: username}) do
    JWT.sign(@jwk, %{username: username}) |> JOSE.JWS.compact() |> elem(1)
  end

  def verify_token(token) do
    case JWT.verify(@jwk, token) do
      {true, %JOSE.JWT{fields: fields}, _jws} ->
        {:ok, fields}

      {false, _jwt, _jws} ->
        {:error, "invalid token"}
    end
  end

  @doc """
  Creates a user.

  ## Examples

      iex> create_user(%{field: value})
      {:ok, %User{}}

      iex> create_user(%{field: bad_value})
      {:error, %Ecto.Changeset{}}

  """
  def create_user(attrs \\ %{}) do
    %User{}
    |> User.changeset(attrs)
    |> Repo.insert()
  end

  def register_user(attrs \\ %{}) do
    %User{}
    |> User.registration_changeset(attrs)
    |> Repo.insert()
  end

  @doc """
  Updates a user.

  ## Examples

      iex> update_user(user, %{field: new_value})
      {:ok, %User{}}

      iex> update_user(user, %{field: bad_value})
      {:error, %Ecto.Changeset{}}

  """
  def update_user(%User{} = user, attrs) do
    user
    |> User.changeset(attrs)
    |> Repo.update()
  end

  @doc """
  Deletes a user.

  ## Examples

      iex> delete_user(user)
      {:ok, %User{}}

      iex> delete_user(user)
      {:error, %Ecto.Changeset{}}

  """
  def delete_user(%User{} = user) do
    Repo.delete(user)
  end

  @doc """
  Returns an `%Ecto.Changeset{}` for tracking user changes.

  ## Examples

      iex> change_user(user)
      %Ecto.Changeset{data: %User{}}

  """
  def change_user(%User{} = user, attrs \\ %{}) do
    User.changeset(user, attrs)
  end

  def registration_change_user(%User{} = user, attrs \\ %{}) do
    User.registration_changeset(user, attrs)
  end
end
