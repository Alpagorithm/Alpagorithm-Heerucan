//
//  main.swift
//  문자열 내 p와 y의 개수 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation


func solution5(_ s:String) -> Bool {
    var pCount = 0
    var yCount = 0

    let arr = s.map { String($0) }

    arr.forEach { str in
        if str == "p" || str == "P" {
            pCount += 1
        } else if str == "y" || str == "Y" {
            yCount += 1
        }
    }

    if pCount != yCount {
        return false
    } else {
        return true
    }
}
solution5("pPoooyY")
