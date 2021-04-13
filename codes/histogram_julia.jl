#using Gadfly
using Plots

function get_bin_edges(a, bins)
    bin_edges = zeros(bins)
    a_min = minimum(a)
    a_max = maximum(a)
    delta = (a_max - a_min) / bins
    for i in 1:size(bin_edges)[1]
        bin_edges[i] = a_min + i*delta
    end

    bin_edges[lastindex(bin_edges)] = a_max

    return bin_edges
end

function compute_bin(x, bin_edges)
    # assuming uniform bins for now
    n = size(bin_edges)[1]
    a_min = bin_edges[1]
    a_max = last(bin_edges)

    # special case to mirror NumPy behavior for last bin
    if x == a_max
        return n # a_max always in last bin
    end

    bin = Int(floor(n * (x - a_min) / (a_max - a_min)))

    if bin < 0 || bin >= n
        return NaN
    else
        return bin
    end
end


function get_histogram(a, bins)
    hist = zeros(bins)
    bin_edges = get_bin_edges(a, bins)

    for x in a[:]
        bin = compute_bin(x, bin_edges)
        if !isnan(bin)
            hist[Int(floor(bin))] += 1
        end
    end

    return hist, bin_edges
end

#Test the Functions
a = rand(100)
h = get_histogram(a, 5)

bar(h[1])
histogram(a, bins = 5)
