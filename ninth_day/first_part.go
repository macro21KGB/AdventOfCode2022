package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Point struct {
	x int
	y int
}

func (p Point) Distance(other Point) int {
	return int(math.Abs(float64(p.x-other.x)) + math.Abs(float64(p.y-other.y)))
}

func (p Point) IsDiagonal(other Point) bool {
	return p.x != other.x && p.y != other.y
}

func get_input(path string) []string {
	file, err := os.ReadFile(path)
	if err != nil {
		fmt.Println(err)
	}
	var text_file = string(file)

	return strings.Split(text_file, "\n")

}

func get_command(command string) (string, int) {
	var direction = string(command[0])
	var distance = string(command[2:])

	// convert distance to int
	var distance_int, err = strconv.Atoi(strings.Replace(distance, "\r", "", -1))
	if err != nil {
		fmt.Println(err)
		return "", 0
	}

	return direction, distance_int
}

func move_tail_to_head(tail *Point, head Point, visited_points *map[Point]bool) {
	// check if head is on the same y axis as tail
	if visited_points != nil && !(*visited_points)[*tail] {
		fmt.Println("adding", tail, "to visited points")
		(*visited_points)[*tail] = true
	}

	if head.y == tail.y {
		if tail.x < head.x {
			tail.x++
		} else {
			tail.x--
		}

	} else if head.x == tail.x {
		if tail.y < head.y {
			tail.y++
		} else {
			tail.y--
		}

	} else {
		// move diagonally
		if tail.y < head.y {
			tail.y++
		} else {
			tail.y--
		}

		if tail.x < head.x {
			tail.x++
		} else {
			tail.x--
		}

	}
	if visited_points != nil && !(*visited_points)[*tail] {
		fmt.Println("adding", tail, "to visited points")
		(*visited_points)[*tail] = true
	}

	fmt.Println("moving tail to head: ", tail, " -> ", head)
}

func solve1(movements []string) {

	var head = Point{0, 0}
	var tail = Point{0, 0}
	var visited_points = make(map[Point]bool)

	for _, move := range movements {
		command, distance := get_command(move)

		switch command {
		case "R":
			head.x += distance
		case "L":
			head.x -= distance
		case "U":
			head.y += distance
		case "D":
			head.y -= distance
		}

		if head.Distance(tail) == 2 && head.IsDiagonal(tail) {
			continue
		}

		for tail.Distance(head) > 1 {
			move_tail_to_head(&tail, head, &visited_points)
		}
	}

	visited_points[Point{0, 0}] = true
	fmt.Println(len(visited_points))
}

func solve2(movements []string) {
	var rope = make([]Point, 2)
	var visited_points = make(map[Point]bool)

	for _, move := range movements {
		command, distance := get_command(move)

		tail := rope[0]
		head := rope[len(rope)-1]

		switch command {
		case "R":
			rope[1].x += distance
		case "L":
			rope[1].x -= distance
		case "U":
			rope[1].y += distance
		case "D":
			rope[1].y -= distance
		}

		if len(rope) < 10 {
			var new_head = Point{head.x, head.y}
			rope = append(rope, new_head)

		} else {
			rope = append(rope[1:], Point{head.x, head.y})
		}

		for i, point := range rope {
			if i == 0 {
				continue
			}

			if point.Distance(tail) == 2 && point.IsDiagonal(tail) {
				continue
			}

		}
	}

	fmt.Println(len(visited_points))
}

func main() {

	var movements = get_input("test_input_large.txt")
	// solve1(movements)
	solve2(movements)
}
