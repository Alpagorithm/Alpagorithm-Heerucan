//
//  main.swift
//  Algorithm
//
//  Created by heerucan on 2022/10/04.
//

import Foundation

var N = readLine()

if let input = N {
    let arr = input.map({ $0 })
    var result: [Int] = []

    if let firstIndex = arr.firstIndex(of: "-") {

        let minus = arr.split(separator: "-").map { String($0) }
        print(minus)

        // minus.map { Int($0)! }.reduce(0, +) +
        for i in minus {
            let plus = i.split(separator: "+").map { Int($0)! }
            print(plus)
            result.append(plus.reduce(0, +))
        }
        print(result.reduce(result[0], -))

    } else {
        let plus = arr.split(separator: "+").map { String($0) }.map { Int($0)! }
        print(plus.reduce(0, +))
    }



}

