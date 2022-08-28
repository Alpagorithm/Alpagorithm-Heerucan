//
//  main.swift
//  정수 제곱근 판별 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

import Foundation
func solution(_ n:Int64) -> Int64 {
    let value = Int64(sqrt(Double(n)))
    if value*value == n {
        return (value + 1) * (value + 1)
    }
    return -1
}
