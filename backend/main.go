package main

import (
	"net/http"
)

// return main page
func mainPage(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("mainpage\n"))
}

// dijkstra implementation
func findRoute(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("findroute\n"))
}

func main() {
	http.HandleFunc("/",mainPage)
	http.HandleFunc("/route",findRoute)
	http.ListenAndServe(":8080",nil)
}