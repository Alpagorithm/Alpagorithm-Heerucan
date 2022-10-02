//
//  main.swift
//  정수내림차순으로배치하기 - level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

let arr = String(n).map { String($0)}.sorted(by: >).joined(separator: "")

return Int64(arr)!
