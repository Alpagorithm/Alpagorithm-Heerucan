//
//  main.swift
//  두정수사이의합 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

func solution(_ a:Int, _ b:Int) -> Int64 {
    if a != b {
        var answer = 0
        if a < b {
            for i in a...b {
                answer += i
            }
        } else {
            for i in b...a {
                answer += i
            }
        }
        return Int64(answer)
    } else {
        return Int64(a)
    }
}
