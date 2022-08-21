//
//  main.swift
//  약수의 개수와 덧셈 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation


func solution(_ left:Int, _ right:Int) -> Int {
    func findCount(_ num: Int) -> Int {
        return Array(1...num).filter{num % $0 == 0}.count
    }
    
    var sum = 0

    for i in left...right {
        if findCount(i) % 2 == 0 {
            sum += i
        } else {
            sum -= i
        }
    }
    return sum
}

solution(13, 17)
