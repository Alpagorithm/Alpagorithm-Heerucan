//
//  main.swift
//  x만큼 간격이 있는 n개의 숫자 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation


func solution6(_ x:Int, _ n:Int) -> [Int64] {
    var answer: [Int64] = []
    var val: Int = 0
    while val != x*n {
        val += x
        answer.append(Int64(val))
    }
    return answer
}

solution6(2, 5)
