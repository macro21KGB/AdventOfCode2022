package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Command struct {
	command         string
	value           int
	time_to_execute int
}

func get_command(command string) Command {
	// split command and value
	splitted_command := strings.Split(command, " ")

	if len(splitted_command) == 1 {
		return Command{strings.Trim(splitted_command[0], "\r"), 0, 1}
	}

	converted_value, err := strconv.Atoi(strings.Trim(splitted_command[1], "\r"))
	if err != nil {
		fmt.Println(err)
	}

	return Command{splitted_command[0], converted_value, 2}

}

func calculate_strength(register int, cycle int) int {
	return register * cycle
}

type CRT struct {
	rows []string
}

func (crt CRT) Print() {
	for _, row := range crt.rows {
		fmt.Println(row)
	}
}

func get_input(path string) []string {
	file, err := os.ReadFile(path)
	if err != nil {
		fmt.Println(err)
	}
	var text_file = string(file)

	return strings.Split(text_file, "\n")

}

func execute_command(command Command, x_register *int) {
	*x_register += command.value

}

func solve1(commands []Command) int {
	// execute commands
	x_register := 1
	cycle := 1
	executing := true
	cycle_tag := 20

	var command_to_execute Command = commands[0]
	target_cycle := cycle + command_to_execute.time_to_execute

	strengths := make([]int, 0)

	for len(commands) > 0 {

		if cycle == target_cycle {
			execute_command(command_to_execute, &x_register)
			executing = false
		}

		if !executing {
			commands = commands[1:]
			if len(commands) != 0 {
				command_to_execute = commands[0]
				target_cycle = cycle + command_to_execute.time_to_execute
				executing = true
			}
		}

		if cycle == cycle_tag {
			strengths = append(strengths, calculate_strength(x_register, cycle))
			cycle_tag += 40
		}
		cycle++
	}

	fmt.Println("FINAL CYCLE: ", cycle)
	fmt.Println(strengths)

	// sum strengths
	sum := 0
	for _, strength := range strengths {
		sum += strength
	}

	return sum
}

func (crt *CRT) draw_pixel(pos int, scanline_index int) {
	first_half := (crt.rows[scanline_index])[:pos]
	second_half := (crt.rows[scanline_index])[pos+1:]
	crt.rows[scanline_index] = first_half + "#" + second_half

}

func (crt *CRT) Init() {
	for i := 0; i < 6; i++ {
		crt.rows = append(crt.rows, strings.Repeat(".", 40))
	}

}

// ---- SOLUTION 2 ----
func solve2(commands []Command) {
	// execute commands
	x_register := 1
	cycle := 1
	executing := true

	crt := CRT{}
	crt.Init()

	current_scanline_index := 0

	var command_to_execute Command = commands[0]
	target_cycle := cycle + command_to_execute.time_to_execute

	for len(commands) > 0 {

		if cycle == target_cycle {
			execute_command(command_to_execute, &x_register)
			executing = false
		}

		if !executing {
			commands = commands[1:]
			if len(commands) != 0 {
				command_to_execute = commands[0]
				target_cycle = cycle + command_to_execute.time_to_execute
				executing = true
			}
		}

		if cycle%40 == 0 {
			current_scanline_index++
			fmt.Println("SCANLINE: ", current_scanline_index)
		}

		crt.draw_pixel(cycle%40-1, current_scanline_index)

		cycle++
	}

	crt.Print()

}

func main() {
	inputs := get_input("input.txt")

	// put commands into a stack
	var commands []Command
	for _, command := range inputs {
		commands = append(commands, get_command(command))
	}

	// fmt.Println("SOLUTION 1: ", solve1(commands))

	solve2(commands)

}
