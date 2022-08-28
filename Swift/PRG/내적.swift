//
//  main.swift
//  내적 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

func solution(_ A:[Int], _ B:[Int]) -> Int {
    var sum = 0
    for index in A.indices {
        sum += (A[index] * B[index])
    }
    return sum
}
