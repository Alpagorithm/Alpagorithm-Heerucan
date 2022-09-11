//
//  main.swift
//  하샤드수 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation


func solution(_ x:Int) -> Bool {
    var result = 0
    result += (x / 1000) + ((x%1000) / 100) + (((x%1000) % 100) / 10) + (((x%1000) % 100) % 10)
    
    if x % result == 0 {
        return true
    } else {
        return false
    }
}
