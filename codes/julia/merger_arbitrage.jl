# Define a struct for Merger Arbitrage parameters
struct MergerArbitrage
    target_shares::Int       # Number of target shares purchased
    acquirer_shares_short::Int # Number of acquirer shares shorted
    target_price::Float64    # Current price of target shares
    acquirer_price::Float64  # Current price of acquirer shares
    offer_ratio::Float64     # Exchange ratio (e.g., 1:1, 2:1, etc.)
    target_price_failure::Float64 # Expected price of target shares if merger fails
end

# Function to calculate payoff when merger succeeds
function calculate_success_payoff(params::MergerArbitrage)
    # Calculate cost of buying target shares
    cost_of_target = params.target_shares * params.target_price
    
    # Calculate proceeds from short selling acquirer shares
    proceeds_from_short = params.acquirer_shares_short * params.acquirer_price
    
    # Calculate value of converted acquirer shares from target shares (post-merger)
    converted_acquirer_shares = params.target_shares / params.offer_ratio
    value_of_converted_acquirer_shares = converted_acquirer_shares * params.acquirer_price
    
    # Use converted shares to cover short position (proceeds already received)
    payoff = value_of_converted_acquirer_shares - cost_of_target + proceeds_from_short
    
    return payoff
end

# Function to calculate payoff when merger fails
function calculate_failure_payoff(params::MergerArbitrage)
    # Calculate cost of buying target shares
    cost_of_target = params.target_shares * params.target_price
    
    # Calculate proceeds from short selling acquirer shares
    proceeds_from_short = params.acquirer_shares_short * params.acquirer_price
    
    # Calculate value of target shares after failure (expected drop in price)
    value_of_target_after_failure = params.target_shares * params.target_price_failure
    
    # Calculate cost to cover short position (repurchase acquirer shares)
    cost_to_cover_short = params.acquirer_shares_short * params.acquirer_price
    
    # Net payoff in case of failure
    payoff = value_of_target_after_failure - cost_to_cover_short + proceeds_from_short - cost_of_target
    
    return payoff
end

# Example Usage

# Define parameters for the merger arbitrage scenario
params = MergerArbitrage(
    20000,          # target_shares
    10000,          # acquirer_shares_short
    19.0,           # target_price
    42.0,           # acquirer_price
    2.0,            # offer_ratio
    15.0            # target_price_failure
)
# Calculate payoffs for both scenarios
success_payoff = calculate_success_payoff(params)
failure_payoff = calculate_failure_payoff(params)

# Print results
println("Payoff if merger succeeds: \$$(success_payoff)")
println("Payoff if merger fails: \$$(failure_payoff)")
