defmodule RPNCalculator.Exception do
  defmodule DivisionByZeroError do
    defexception message: "division by zero occurred"
  end

  defmodule StackUnderflowError do
    @message "stack underflow occurred"
    defexception message: @message
    
    @impl true

    def exception([]) do
      %StackUnderflowError{}
    end

    def exception(context) do
      %StackUnderflowError{message: @message <> ", context: #{context}"}
    end
  end
  
  def divide([]) do
    raise StackUnderflowError, "when dividing"
  end
  
  def divide([_]) do
    raise StackUnderflowError, "when dividing"
  end
  
  def divide([0, _]) do
    raise DivisionByZeroError
  end
  
  def divide([a, b]) do
    b / a
  end
end
