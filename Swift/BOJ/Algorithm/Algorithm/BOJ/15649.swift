//
//  15649.swift
//  Algorithm
//
//  Created by heerucan on 2022/10/30.
//

import Foundation

let input = readLine()!.components(separatedBy: " ").map { Int($0)! }
let (n, m) = (input[0], input[1])

var used = Array(repeating: false, count: n+1)

func dfs(_ length: Int, _ stack: [String]) {
    if length == m {
        print(stack.joined(separator: " "))
        return
    }

    for i in 1...n {
        if used[i] { continue }
        used[i] = true
        dfs(length + 1, stack + [String(i)])
        used[i] = false
    }
}

dfs(0, [])
