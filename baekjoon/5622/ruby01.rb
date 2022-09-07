class String
  @@phonenum = {
    'A' => 2, 'B' => 2
  }
  def to_phonenum
    return 2 if "ABC".include? self
    return 3 if "DEF".include? self
    return 4 if "GHI".include? self
    return 5 if "JKL".include? self
    return 6 if "MNO".include? self
    return 7 if "PQRS".include? self
    return 8 if "TUV".include? self
    return 9 if "WXYZ".include? self
    raise "NoMatchingPhonenumError"
  end
end

class Integer
  def to_phoneweight
    self + 1
  end
end

puts gets.chomp.split("").map(&:to_phonenum).map(&:to_phoneweight).sum
