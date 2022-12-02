package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"sort"
	"strconv"
	"strings"
)

func check(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func sum_slice(slice []int) int {
	sum := 0
	for i := 0; i < len(slice); i++ {
		sum += slice[i]
	}
	return sum
}

func max(slice []int) int {
	max := 0
	for i := 0; i < len(slice); i++ {
		if slice[i] > max {
			max = slice[i]
		}
	}
	return max
}

func main() {
	// read file content
	content, err := ioutil.ReadFile("./input.txt")
	check(err)
	// convert ot string
	str_content := string(content)

	// split content on \n character
	str_content_split := strings.Split(str_content, "\n")

	// create list of lists of elf snack calories
	elf_index := 0
	elf_calories := [][]int{}
	curr_slice := []int{}
	for i := 0; i < len(str_content_split); i++ {
		if len(elf_calories) != (elf_index) && (i > 0) {
			elf_calories = append(elf_calories, curr_slice)
			curr_slice = []int{}
		}
		if str_content_split[i] == "" {
			elf_index += 1
		} else {
			val, err := strconv.Atoi(str_content_split[i])
			check(err)
			curr_slice = append(curr_slice, val)
		}
	}

	// calculate sum of all snacks carried by each elf
	sum_elf_calories := []int{}
	for i := 0; i < len(elf_calories); i++ {
		sum_elf_calories = append(sum_elf_calories, sum_slice(elf_calories[i]))
	}

	// calculate max of snack calories for all elves (find top 1 calories)
	max_calories := max(sum_elf_calories)

	// print the answer to part 1
	fmt.Printf("Max Calories for 1 elf: %d\n", max_calories)

	// sort the slice in descending order
	sort.Slice(sum_elf_calories, func(i, j int) bool {
		return sum_elf_calories[i] > sum_elf_calories[j]
	})

	// select the top 3 elves by sum of calories
	top_three_elves := sum_elf_calories[0:3]

	// sum the calories for the top 3 elves
	max_3_calories := sum_slice(top_three_elves)

	// print the answer to part 2
	fmt.Printf("Max Calories for 3 elves: %d\n", max_3_calories)

}
