//
//  2579.swift
//  Algorithm
//
//  Created by heerucan on 2022/11/06.
//

import Foundation

struct b2579 {
    static func run() {
        var n = Int(readLine()!)! // 계단개수
        var nArray = Array(repeating: 0, count: n) // 계단 마다 배점
        var d = Array(repeating: 0, count: n)

        for i in 0...n-1 {
            nArray[i] = Int(readLine()!)!
        }
        
        if n == 1 {
            print(nArray[0])
        } else if n == 2 {
            print(nArray[0] + nArray[1])
        } else if n == 3 {
            print(max(nArray[2] + nArray[0], nArray[2] + nArray[1])) // 1+3 or 2+3인지
        } else {
            d[0] = nArray[0] // 첫번째는 무조건 밟아야 올라감
            d[1] = nArray[0] + nArray[1] // 두번째도 무조건 다 밟을 수 밖에 없음
            d[2] = max(nArray[2] + nArray[0], nArray[2] + nArray[1]) // 1+3 or 2+3인지

            for i in 3...n-1 {
                d[i] = max(nArray[i] + nArray[i-1] + d[i-3], nArray[i] + d[i-2])
            }
            print(d[n-1])
        }
    }
}

b2579.run()
