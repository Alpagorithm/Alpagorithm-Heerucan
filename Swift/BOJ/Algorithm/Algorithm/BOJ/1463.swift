//
//  1463.swift
//  Algorithm
//
//  Created by heerucan on 2022/10/10.
//

import Foundation

var N = readLine()

if let input = Int(N!) {
    var dp = [Int](repeating: 0, count: 1000001)
    for i in 2..<input+1 {
        dp[i] = dp[i-1]+1
        
        if i % 2 == 0 {
            dp[i] = min(dp[i], dp[i/2]+1)
        }
        
        if i % 3 == 0 {
            dp[i] = min(dp[i], dp[i/3]+1)
        }
    }
    print(dp[input])
}
