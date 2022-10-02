//
//  main.swift
//  신규아이디추천- level1
//
//  Created by heerucan on 2022/08/14.
//

import Foundation

func solution(_ new_id:String) -> String {
    
    // 1단계 소문자로 바꾸기
    // 2단계 특수문자 제거하기
    var arr = new_id.lowercased().components(separatedBy: ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", "[", "{", "]", "}", ":", "?", ",", "<", ">", "/"]).joined()
    
    // 3단계 .. 치환
    while arr.contains("..") {
        arr = arr.replacingOccurrences(of: "..", with: ".").trimmingCharacters(in: ["."])
    }
    
    // 4단계 마침표 처음끝 제거
    arr = arr.trimmingCharacters(in: ["."])
    
    // 5단계 빈문자열 대신 "a" 넣기
    if arr.isEmpty {
        arr = "a"
    }
    
    // 6단계 16자 이상
    // 7단계 2자 이하
    if arr.count == 1 {
        return arr + arr + arr
    } else if arr.count == 2 {
        return String(arr + String(arr.last!))
    } else if arr.count >= 16 {
        arr = arr.prefix(15).trimmingCharacters(in: ["."]).map { String($0) }.joined()
        return arr
    } else {
        return arr
    }
}

solution("...!@BaT#*..y.abcdefghijklm")

// 정규식 또는 각 단계 별로 함수를 만들어서 풀어도 될 것 같다.
// 무작정 고차함수를 사용해서 푸는 건 좋지 못한 것 같음
// 문자열 관련 메소드에 대한 이해가 필요할 것 같다.
