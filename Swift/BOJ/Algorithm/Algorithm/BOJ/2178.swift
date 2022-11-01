//
//  2178.swift
//  Algorithm
//
//  Created by heerucan on 2022/11/01.
//

import Foundation

// MARK: - BFS

struct b2178 {
    static func run() {
        // 2차원 리스트의 보드 정보를 입력 받기
        let input = readLine()!.components(separatedBy: " ").map { Int($0)! }
        var board = [[Int]](repeating: [], count: input[0])
        
        for i in 0..<input[0] {
            let v = readLine()!.map { Int("\($0)")! }
            board[i].append(contentsOf: v)
        }
        
        // 상하좌우 네 가지 이동 방향 정의하기
        let dx = [-1, 1, 0, 0]
        let dy = [0, 0, -1, 1]
        
        var queue = [[0,0]] // 큐
        var visited = [[Bool]](repeating: [Bool](repeating: false, count: input[1]),
                               count: input[0]) // 방문했는지 확인
        
        var nx = 0
        var ny = 0
        
        // 시작좌표 세팅
        var x = queue[0][0]
        var y = queue[0][1]
        visited[0][0] = true
        
        while !queue.isEmpty { // 큐가 빌 때까지 반복하기!
            x = queue[0][0]
            y = queue[0][1]
            
            queue.removeFirst() // append로 넣을 것이라서 FIFO 적용
            
            for i in 0..<4 { // 현재 위치에서 상하좌우 체크하는 것 - 0123
                // 이동 가능한 좌표 계산
                // (0, 0)이라고 치면  dx = [-1, 1, 0, 0] | dy = [0, 0, -1, 1]
                // -1인 것은 미로의 벽이라고 생각하면 됨..
                nx = x + dx[i]
                ny = y + dy[i]
                
                // 좌표가 board의 좌표를 벗어나지 않으면
                // 보드 안에 다음 번 좌표가 위치하고, 이전에 방문한 장소가 아니다
                if nx >= 0 && ny >= 0 && nx < input[0] && ny < input[1] &&
                    visited[nx][ny] == false {
                    
                    if board[nx][ny] == 1 { // 보드의 좌표가 이동가능한 값이다. == 1
                        queue.append([nx, ny]) // 큐에 넣어주고
                        board[nx][ny] = board[x][y] + 1 // 총 이동거리 계산
                        visited[nx][ny] = true // 방문한 곳은 true로 변경
                    }
                }
            }
        }
        // 왜 -1씩 해주냐면 실제적으로 (1,1)로 시작한 거지만 좌표상 (0,0)임
        print(board[input[0]-1][input[1]-1])
    }
}

b2178.run()
