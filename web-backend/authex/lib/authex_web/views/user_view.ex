defmodule AuthexWeb.UserView do
  use AuthexWeb, :view
  alias AuthexWeb.UserView

  def render("index.json", %{users: users}) do
    %{data: render_many(users, UserView, "user.json")}
  end

  def render("show.json", %{user: user}) do
    %{data: render_one(user, UserView, "user.json")}
  end

  def render("user.json", %{user: user, token: token}) do
    %{
      name: user.name,
      username: user.username,
      token: token
    }
  end

  def render("user.json", %{user: user}) do
    %{
      name: user.name,
      username: user.username
    }
  end
end
