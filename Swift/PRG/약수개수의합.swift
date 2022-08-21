//
//  main.swift
//  약수개수의합 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

func solution(_ n:Int) -> Int {
    var array: [Int] = []
    for i in 1...n {
        if n % i == 0 {
            array.append(i)
        }
    }
    return array.reduce(0, +)
}
