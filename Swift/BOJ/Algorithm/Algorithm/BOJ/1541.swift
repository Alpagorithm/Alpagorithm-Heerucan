//
//  1541.swift
//  Algorithm
//
//  Created by heerucan on 2022/10/11.
//

import Foundation

var N = readLine()
var total = 0

if let input = N {
    let minus = input.map({ $0 }).split(separator: "-").map { String($0) }
    for (index, i) in minus.enumerated() {
        if index == 0 && !i.contains("+") {
            total += Int(i)!
        } else if index == 0 && i.contains("+") {
            total += i.map { $0 }.split(separator: "+").map { String($0) }.map { Int($0)! }.reduce(0, +)
        } else if i.contains("+") {
            total -= i.map { $0 }.split(separator: "+").map { String($0) }.map { Int($0)! }.reduce(0, +)
        } else {
            total -= Int(i)!
        }
    }
    print(total)
}
