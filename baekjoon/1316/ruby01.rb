class String
  def is_groupword?
    cs = self.split("")
    character_stack = []
    cs.each do |c|
      next if character_stack[-1] == c
      character_stack << c and next unless character_stack.include? c
      return false
    end
    true
  end
end

puts $<.map(&:chomp)[1..].map(&:is_groupword?).count(&:itself)