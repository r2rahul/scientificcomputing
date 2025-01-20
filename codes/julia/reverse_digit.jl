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

# A functional programming style to reverse the integer number
function reverse_digit_func(number)
    # Helper function to get digits in reverse order
    function get_reversed_digits(n)
        n == 0 ? [] : [n % 10; get_reversed_digits(div(n, 10))]
    end
    
    # Reconstruct the number from reversed digits
    foldl((acc, digit) -> acc * 10 + digit, get_reversed_digits(number))
end

println("Enter the integer number")
n = readline()
n = parse(Int64, n)
println("Imperative Programming Style")
println(reverse_digit(n))
println("Functional Programming Style")
println(reverse_digit_func(n))