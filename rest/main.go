package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	log.Println("Starting up server")

	router := NewRouter()
	router.Use(loggingMiddleware)
	log.Fatal(http.ListenAndServe(":8080", router))
}

func loggingMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		log.Println(fmt.Sprintf("%s %s", r.Method, r.URL))
		next.ServeHTTP(w, r)
	})
}
