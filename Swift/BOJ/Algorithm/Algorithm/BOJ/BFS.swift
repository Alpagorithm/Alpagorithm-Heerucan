//
//  BFS.swift
//  Algorithm
//
//  Created by heerucan on 2022/10/11.
//

import Foundation

let graph: [String: [String]] = [
    "A" : ["B", "C"],
    "B" : ["A", "D", "E"],
    "C" : ["A", "F"],
    "D" : ["B"],
    "E" : ["B"],
    "F" : ["C"],
]

func BFS(graph: [String: [String]], start: String) -> [String] {
    var visitedQueue: [String] = [] // 이미 방문한 노드
    var needVisitiedQueue: [String] = [] // 방문이 필요한 노드
    
    // 방문해야 할 노드의 개수가 0이 될 때까지
    while needVisitiedQueue.count != 0 {
        // 방문이 필요한 노드가 있는 첫 번째 큐에서 빼서
        let node = needVisitiedQueue.removeFirst()
        // 해당 노드가 이미 방문한 큐에 겹치지 않으면 큐에 추가
        if !visitedQueue.contains(node) {
            visitedQueue.append(node)
            needVisitiedQueue.append(contentsOf: graph[node]!)
        }
    }
    return visitedQueue
}
