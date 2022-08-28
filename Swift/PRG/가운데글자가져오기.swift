//
//  main.swift
//  가운데글자가져오기 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

func solution(_ s:String) -> String {
    // 글자수가 짝수면 가운데 2개
    if Array(s).count%2 == 0 {
        return String(Array(s)[(s.count/2)-1...(s.count/2)])
    // 글자수가 홀수면 가운데 1개
    } else {
        return String(Array(s)[(s.count/2)])
    }
}
