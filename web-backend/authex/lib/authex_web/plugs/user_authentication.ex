defmodule AuthexWeb.Plug.UserAuthentication do
  import Plug.Conn
  require Logger
  alias Authex.Accounts

  def init(defaults) do
    defaults
  end

  def call(conn, _opts) do
    with ["Bearer " <> token] <- get_req_header(conn, "authorization"),
         {:ok, %{"username" => username}} <- Accounts.verify_token(token) do
      conn
      |> assign(:current_username, username)
    else
      _ ->
        conn
        |> put_status(:unauthorized)
        |> Phoenix.Controller.put_view(AuthexWeb.ErrorView)
        |> Phoenix.Controller.render(:"401")
        |> halt()
    end
  end
end
