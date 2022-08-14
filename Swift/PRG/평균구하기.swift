//
//  main.swift
//  평균구하기 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

func solution(_ arr:[Int]) -> Double {
    var sum = 0
    arr.map { sum += $0 }
    return Double(sum)/Double(arr.count)
}
