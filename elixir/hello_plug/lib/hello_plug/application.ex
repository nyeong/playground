defmodule HelloPlug.Application do
  use Application
  require Logger

  def start(_type, _args) do
    children = [
      {Plug.Cowboy, scheme: :http, plug: HelloPlug.Router,
        options: [port: 8080]}
    ]

    opts = [strategy: :one_for_one, name: HelloPlug.Supervisor]

    Logger.info("Server is listen on port 8080")

    Supervisor.start_link(children, opts)
  end
end
