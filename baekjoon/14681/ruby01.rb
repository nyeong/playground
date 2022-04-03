class Point
  def initialize x, y
    @x = x
    @y = y
  end

  def on_quadrant
    return 1 if @x > 0 and @y > 0
    return 2 if @x < 0 and @y > 0
    return 3 if @x < 0 and @y < 0
    return 4 if @x > 0 and @y < 0
    return nil
  end
end


X = gets.to_i
Y = gets.to_i

p = Point.new X, Y
puts p.on_quadrant
