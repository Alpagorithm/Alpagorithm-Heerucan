//
//  main.swift
//  나누어 떨어지는 숫자 배열 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
    var resultArr: [Int] = []
    resultArr = arr.filter { $0%divisor == 0 }
    resultArr = resultArr.sorted(by: <)
    if resultArr.count == 0 {
        return [-1]
    }
    return resultArr
}
