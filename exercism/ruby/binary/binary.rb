=begin
Write your code for the 'Binary' exercise in this file. Make the tests in
`binary_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/binary` directory.
=end
module Binary
    def self.to_decimal str
        l = str.length - 1
        str.each_char.each_with_index.reduce(0) do |acc, base_with_index|
            base_number, index = Integer(base_with_index[0]), base_with_index[1]
            acc + base_number * 2 ** (l - index)
        end
    end
end
