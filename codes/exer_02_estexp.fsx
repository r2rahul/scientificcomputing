// For more information see https://aka.ms/fsharp-console-apps
open System
open System.IO
open System.Numerics

let factorialI (n: int): BigInteger =
    match n with
    | n when n < 0 -> failwith "Factorial is not defined for negative numbers"
    | 0 | 1 -> BigInteger.One
    | _ ->
        seq { 2 .. n }
        |> Seq.fold (fun acc x -> BigInteger.Multiply(acc, BigInteger(x))) BigInteger.One

        
let factorialF k = [|1..k|] |> Array.fold (*) 1 |> float
let estimateExp x n =
    [|0..n|]
    |> Array.map (fun k -> (x ** float k) / factorialF k)
    |> Array.sum

// Example usage
let x = 1.0
let n = 10
let estimate = estimateExp x n
printfn "Estimate of e^%.1f using %d terms: %f" x n estimate
