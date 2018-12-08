package main

import (
	"garden-rest/views"
	"net/http"

	"github.com/gorilla/mux"
)

type Route struct {
	Name        string
	Method      string
	Pattern     string
	HandlerFunc http.HandlerFunc
}

type Routes []Route

func NewRouter() *mux.Router {

	router := mux.NewRouter().StrictSlash(true)

	for _, domain := range domains {

		for _, route := range domain {
			router.
				Methods(route.Method).
				Path(route.Pattern).
				Name(route.Name).
				Handler(route.HandlerFunc)
		}
	}

	return router
}

var plantRoutes = Routes{
	Route{
		Name:        "Get all plants",
		Method:      "GET",
		Pattern:     "/plants",
		HandlerFunc: views.GetAllPlants,
	},
}

var potRoutes = Routes{
	Route{
		Name:        "Get all pots",
		Method:      "GET",
		Pattern:     "/pots",
		HandlerFunc: views.GetAllPlants,
	},
}

var domains = []Routes{
	plantRoutes,
}
