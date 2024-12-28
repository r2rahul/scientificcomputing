open System
open System.IO
// F# exercism on monte carlo method
// read config file to get no of simualtion

// set number of simulation
let noOfSim = 1000000
let seed = 42
let random = Random(seed)
let totalSim = seq {
    for i in 1..noOfSim do
        let x = random.NextDouble()
        let y = random.NextDouble()
        if x * x + y * y <= 1.0 then
            yield 1.0
        else 
            yield 0.0
    }

let totalSum = totalSim |> Seq.sum
let pi = 4.0 * (float totalSum / float noOfSim)

printfn "Value of estimated Pi %0.5f" pi
