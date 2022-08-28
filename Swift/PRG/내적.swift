//
//  main.swift
//  내적 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

func solution(_ A:[Int], _ B:[Int]) -> Int {
    var totalArr: [Int] = []
    for index in A.indices {
        totalArr.append(A[index] * B[index])
    }
    return totalArr.reduce(0, +)
}
