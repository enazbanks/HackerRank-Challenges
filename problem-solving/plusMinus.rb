def plusMinus(arr)
  n = arr.count.to_f

  positive_numbers = []
  negative_numbers = []
  zero_numbers = []

  arr.each do |i|
      if i > 0
          positive_numbers << i
      elsif i < 0
          negative_numbers << i
      else
          zero_numbers << i
      end
  end

  positive_ratio = (positive_numbers.count / n).round(6)
  negative_ratio = (negative_numbers.count / n).round(6)
  zero_ratio = (zero_numbers.count / n).round(6)

  return positive_ratio, negative_ratio, zero_ratio
end

n = gets.strip.to_i
arr = gets.rstrip.split.map(&:to_i)

result = plusMinus(arr)
puts result.join("\n")

puts plusMinus([-4, 3, -9, 0, 4, 1])
