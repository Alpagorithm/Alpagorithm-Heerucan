//
//  main.swift
//  짝수와 홀수 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

func solution(_ n:Int) -> Int {
    func solution(_ num:Int) -> String {
        if num.isMultiple(of: 2) {
            return "Even"
        } else {
            return "Odd"
        }
    }
}
