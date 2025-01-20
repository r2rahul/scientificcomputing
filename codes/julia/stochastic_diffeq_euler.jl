using Random
using Distributed
using Plots
Random.seed!(12)

"""
    Pars

A structure to hold parameters for geometric Brownian motion simulation.

Fields:
- `μ::Float64`: Drift coefficient
- `σ::Float64`: Volatility coefficient
- `T::Float64`: Total time of simulation
- `N::Float64`: Number of time steps
"""
struct Pars 
    μ::Float64
    σ::Float64
    T::Float64
    N::Float64
end

"""
    solution2

A structure to hold the solution of the geometric Brownian motion simulation.

Fields:
- `sol::Vector{Float64}`: Vector of simulated values
- `t::Vector{Float64}`: Vector of time points
"""
struct solution2
    sol::Vector{Float64}
    t:: Vector{Float64}
end

"""
    euler_steps(x::Float64, dt::Float64, pars::Pars)

Perform a single Euler step for geometric Brownian motion.

# Arguments
- `x::Float64`: Current value
- `dt::Float64`: Time step
- `pars::Pars`: Parameters for the simulation

# Returns
- `Float64`: Next value after the Euler step
"""
function euler_steps(x::Float64, dt::Float64, pars::Pars)
    dw = √dt * rand()  # Generate random Wiener process increment
    out = x + pars.μ * x * dt + pars.σ * x * dw  # Euler-Maruyama method
    return out
end

"""
    euler_run(x0::Float64, pars::Pars)

Simulate geometric Brownian motion using the Euler-Maruyama method.

# Arguments
- `x0::Float64`: Initial value
- `pars::Pars`: Parameters for the simulation

# Returns
- `solution2`: Structure containing the simulated values and time points
"""
function euler_run(x0::Float64, pars::Pars)
    dt = Float64(pars.T) / Float64(pars.N)  # Calculate time step
    l = Int64(pars.N + 1.0)  # Total number of points including initial
    t = range(0.0, pars.T, length = l)  # Generate time vector
    sol = zeros(l)  # Initialize solution vector
    sol[1] = x0  # Set initial value
    for i in 1:Int64(pars.N)
        sol[i + 1] = euler_steps(sol[i], dt, pars)  # Perform Euler steps
    end
    return solution2(sol, t) 
end

# Set parameters for the simulation
pars = Pars(0.1, 0.2, 1, 1000);
x0 = 100.0;

# Run the simulation
euler_sol = euler_run(x0, pars)

# Plot the solution
plot(euler_sol.t, euler_sol.sol, title="Geometric Brownian Motion Simulation",
     xlabel="Time", ylabel="Value", label="GBM Path")
