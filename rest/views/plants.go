package views

import (
	"encoding/json"
	"fmt"
	"garden-rest/entities"
	"net/http"

	"github.com/gorilla/mux"
)

//Gets all plants at /plants
func GetAllPlants(w http.ResponseWriter, r *http.Request) {
	todos := entities.Todos{
		entities.Todo{Name: "Write presentation"},
		entities.Todo{Name: "Host meetup"},
	}

	if err := json.NewEncoder(w).Encode(todos); err != nil {
		panic(err)
	}
}

func Index(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Welcome!")
}

func TodoIndex(w http.ResponseWriter, r *http.Request) {

}

func GetSinglePlant(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	todoId := vars["todoId"]
	fmt.Fprintln(w, "Todo show:", todoId)
}
