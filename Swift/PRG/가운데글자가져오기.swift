//
//  main.swift
//  가운데글자가져오기 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

func solution(_ s:String) -> String {
    
    let arr = s.map { $0 }
    
    // 글자수가 짝수면 가운데 2개
    if arr.count%2 == 0 {
        let start = s.index(s.startIndex, offsetBy: arr.count/2-1)
        let end = s.index(s.startIndex, offsetBy: arr.count/2)
        return String(s[start...end])
    // 글자수가 홀수면 가운데 1개
    } else {
        let start = s.index(s.startIndex, offsetBy: arr.count/2)
        return String(s[start])
    }
}
