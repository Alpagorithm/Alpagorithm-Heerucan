//
//  문자열정렬하기2.swift
//  Algorithm
//
//  Created by heerucan on 2022/11/06.
//

import Foundation

func solution(_ my_string: String) -> String {
    return my_string.map { $0.lowercased() }.sorted(by: <).joined()
}

solution("heLLo")
