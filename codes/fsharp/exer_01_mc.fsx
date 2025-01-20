open System

// Initialize the random number generator
let seed = 42
let random = Random(seed)

// Define the function to perform simulation
let totalSim nSim = seq {
    for i in 1..nSim do
        let x = random.NextDouble()
        let y = random.NextDouble()
        if x * x + y * y <= 1.0 then
            yield 1.0
        else 
            yield 0.0
}

[<EntryPoint>]
let main argv =
    if argv.Length = 1 then
        let noOfSim = argv.[0] |> int
        let nSim = totalSim noOfSim
        let totalSum = nSim |> Seq.sum
        let pi = 4.0 * (float totalSum / float noOfSim)
        printfn "Value of estimated Pi %0.5f" pi
        0 // Return 0 to indicate successful execution
    else
        printfn "Please specify a valid integer number for simulation"
        1 // Return 1 to indicate error