//
//  main.swift
//  약수개수의합 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

func solution2(_ n:Int) -> Int {
    if n != 0 {
        var array: [Int] = []
        for i in 1...n {
            if n % i == 0 {
                array.append(i)
            }
        }
        return array.reduce(0, +)
    } else {
        return 0
    }
}

// 개선한 코드

func solution(_ n:Int) -> Int {
    if n == 0 {
        return 0
    } else {
        return Array(1...n).filter { n % $0 == 0 }.reduce(.zero, +)
    }
}
solution(12)
