defmodule RemoteControlCar do
  @enforce_keys [:nickname]
  defstruct battery_percentage: 100,
            distance_driven_in_meters: 0,
            nickname: nil
  @type t :: %__MODULE__{
    battery_percentage: pos_integer(),
    distance_driven_in_meters: pos_integer(),
    nickname: String.t()
  }

  @spec new(String.t()) :: t()
  def new(nickname \\ "none") do
    %__MODULE__{nickname: nickname}
  end

  @spec display_distance(t()) :: none()
  def display_distance(%__MODULE__{distance_driven_in_meters: meters}) do
    "#{meters} meters"
  end

  def display_battery(%__MODULE__{battery_percentage: battery}) when battery > 0 do
    "Battery at #{battery}%"
  end
  def display_battery(%__MODULE__{battery_percentage: battery}) when battery == 0 do
    "Battery empty"
  end

  def drive(%__MODULE__{
    distance_driven_in_meters: meters,
    battery_percentage: battery,
  } = remote_car) when battery > 0 do
    %{remote_car | battery_percentage: battery - 1, distance_driven_in_meters: meters + 20}
  end
  def drive(%__MODULE__{
    battery_percentage: battery,
  } = remote_car) when battery == 0 do
    %{remote_car | battery_percentage: 0, distance_driven_in_meters: 0}
  end
end
