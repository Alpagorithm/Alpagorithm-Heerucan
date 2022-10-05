//
//  1676.swift
//  Algorithm
//
//  Created by heerucan on 2022/10/05.
//

import Foundation

var N = readLine()

if let input = Int(N!) {
    // 소인수분해 2와 5가 있으면 10 -> 1개 count
    // 근데 5가 무조건 2 뒤에 있으니까 5만 count 해주면 됨
    var value = 0
    if input == 0 {
        print(0)
    } else {
        for i in 1...input {
            // 변수를 선언하는 이유는 i는 let이라서 5로 나눠서 값을 줄 수 없음
            var num = i
            
            while num % 5 == 0 {
                value += 1
                num = num/5
            }
        }
        print(value)
    }
}
