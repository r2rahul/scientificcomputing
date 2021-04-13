# A function to reverse the integer number
# Without converting the number to string
function reverse_digit(number)
    y = 0
    while number >= 1
        z = number % 10
        y = 10 * y + z
        number = Int(floor( number / 10))
    end
    return y
end
println("Enter the integer number")
n = readline()
n = parse(Int64, n)
println(reverse_digit(n))
