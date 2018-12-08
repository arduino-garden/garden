package entities

import "time"

type Pot struct {
	ID        string `json:"id,omitempty"`
	Firstname string `json:"firstname,omitempty"`
	Lastname  string `json:"lastname,omitempty"`
}

// This struct represents the DB model of a Plant
type Plant struct {
	ID    string `json:"id,omitempty"`
	City  string `json:"city,omitempty"`
	State string `json:"state,omitempty"`
	Pot   Pot    `json:"state,omitempty"`
}

type Todo struct {
	Name      string    `json:"name"`
	Completed bool      `json:"completed"`
	Due       time.Time `json:"due"`
}

type Todos []Todo
