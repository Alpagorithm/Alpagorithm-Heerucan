//
//  main.swift
//  하샤드수 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation


func solution(_ x:Int) -> Bool {
    var result = 0
    for i in String(x) {
        guard let num = Int(String(i)) else { break }
        result += num
    }
    
    return x % result == 0 ? true : false
}
