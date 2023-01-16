defmodule Authex.Accounts.User do
  use Ecto.Schema
  import Ecto.Changeset

  schema "users" do
    field :name, :string
    field :password_hash, :string
    field :password, :string, virtual: true
    field :username, :string

    timestamps()
  end

  @doc false
  def changeset(user, attrs) do
    user
    |> cast(attrs, [:name, :username])
    |> validate_required([:name, :username])
  end

  def registration_changeset(user, attrs) do
    user
    |> changeset(attrs)
    |> cast(attrs, [:password])
    |> validate_required([:password])
    |> validate_length(:password, min: 6)
    |> hash_password()
  end

  @spec hash_password(Ecto.Changeset) :: Ecto.Changeset
  defp hash_password(cs = %Ecto.Changeset{valid?: true, changes: %{password: password}}) do
    put_change(cs, :password_hash, Pbkdf2.hash_pwd_salt(password))
  end

  defp hash_password(cs = %Ecto.Changeset{}) do
    cs
  end
end
