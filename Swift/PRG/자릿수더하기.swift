//
//  main.swift
//  자릿수 더하기 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

func solution(_ n:Int) -> Int {
    return String(n).map { String($0) }.reduce(0) { $0 + Int($1)! })
}
