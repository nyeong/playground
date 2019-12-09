defmodule HelloPlug.Router do
  use Plug.Router

  plug :match
  plug HelloPlug.VerifyAuth, allows: ["hi"]
  plug :dispatch

  get "/" do
    send_resp(conn, 200, "Welcome")
  end

  match _ do
    send_resp(conn, 404, "Oops!")
  end
end
