//
//  main.swift
//  없는숫자더하기 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

func solution(_ numbers:[Int]) -> Int {
    return 45 - numbers.reduce(0) { $0 + $1 }
}
