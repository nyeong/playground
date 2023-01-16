defmodule AuthexWeb.UserController do
  use AuthexWeb, :controller

  alias Authex.Accounts
  alias Authex.Accounts.User

  action_fallback AuthexWeb.FallbackController

  def login(conn, %{"username" => username, "password" => password}) do
    with {:ok, user} <- Accounts.verify_user_password(username, password),
         token <- Accounts.issue_token(user) do
      conn
      |> render("user.json", user: user, token: token)
    else
      _ ->
        {:error, ""}

      {:error, reason} ->
        {:error, reason}
    end
  end

  def index(conn, _params) do
    users = Accounts.list_users()
    render(conn, "index.json", users: users)
  end

  def create(conn, %{"user" => user_params}) do
    with {:ok, %User{} = user} <- Accounts.create_user(user_params) do
      conn
      |> put_status(:created)
      |> put_resp_header("location", Routes.user_path(conn, :show, user))
      |> render("show.json", user: user)
    end
  end

  def show(conn, %{"id" => id}) do
    user = Accounts.get_user!(id)
    render(conn, "show.json", user: user)
  end

  def update(conn, %{"id" => id, "user" => user_params}) do
    user = Accounts.get_user!(id)

    with {:ok, %User{} = user} <- Accounts.update_user(user, user_params) do
      render(conn, "show.json", user: user)
    end
  end

  def delete(conn, %{"id" => id}) do
    user = Accounts.get_user!(id)

    with {:ok, %User{}} <- Accounts.delete_user(user) do
      send_resp(conn, :no_content, "")
    end
  end
end
