//
//  1764.swift
//  Algorithm
//
//  Created by heerucan on 2022/10/11.
//

import Foundation

let input = readLine()!
let arr = input.split(separator: " ")
var N = Int(arr[0])!
var M = Int(arr[1])!
var nSet = Set<String>()
var mSet = Set<String>()

while N != 0 {
    let name = readLine()!
    nSet.insert(name)
    N -= 1
}

while M != 0 {
    let name = readLine()!
    mSet.insert(name)
    M -= 1
}

print(nSet.intersection(mSet).count)
nSet.intersection(mSet).sorted(by: <).forEach { print($0, separator: "", terminator: "\n") }
