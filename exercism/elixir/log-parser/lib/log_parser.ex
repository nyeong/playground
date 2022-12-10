defmodule LogParser do
  @valid_tags ~w[DEBUG INFO WARNING ERROR]
  @valid_line_regex Regex.compile!("^\\[(#{Enum.join(@valid_tags, "|")})\\] ")
  @split_regex ~r/<(~|\*|=|-)*>/
  @user_name_regex ~r/User\s*(\S*)\s*/

  def valid_line?(line) do
    line =~ @valid_line_regex
  end

  def split_line(line) do
    Regex.split(@split_regex, line)
  end

  def remove_artifacts(line) do
    Regex.replace(~r/end-of-line\d+/i, line, "")
  end

  def tag_with_user_name(line) do
    with {:ok, user_name} <- find_user_name(line) do
      "[USER] #{user_name} " <> line
    else
      _ -> line
    end
  end
  
  defp find_user_name(line) do
    with [_, name] when is_bitstring(name) <- Regex.run(@user_name_regex, line)
    do
      {:ok, name}
    else
      _ -> {:error}
    end
  end
end
