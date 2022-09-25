//
//  main.swift
//  자연수뒤집어배열로만들기 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation


func solution4(_ n:Int64) -> [Int] {
    var a = String(n).reversed().map { String($0) }.map { Int($0)! }
    return a
}
solution4(12345)
