//
//  main.swift
//  나머지가 1이 되는 수 찾기 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

func solution(_ n:Int) -> Int {
    for i in 2...n {
        if n % i == 1 {
            return i
        }
    }
    return 1
}
