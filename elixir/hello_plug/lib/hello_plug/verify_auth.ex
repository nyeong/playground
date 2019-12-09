defmodule HelloPlug.VerifyAuth do
  defmodule RequestNotAllowedError do
    defexception message: ""
  end

  def init(options), do: options

  def call(%Plug.Conn{req_headers: headers} = conn, [allows: allows]) do
    for {"authorization", token} <- headers,
      do: verify_auth!(token, allows)
    IO.puts inspect(headers)
    conn
  end

  defp verify_auth!(token, allow_tokens) do
    unless Enum.any?(allow_tokens, & &1 == token),
      do: raise(RequestNotAllowedError)
  end
end
