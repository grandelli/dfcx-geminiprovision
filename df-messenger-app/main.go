// Package main is the main package
package main

import (
        "log"
        "net/http"
        "os"
        "text/template"
)

var templates *template.Template

func init() {
        templates = template.Must(template.New("").ParseGlob("templates/*"))
}

// indexHandler handles the homepage.
func indexHandler(w http.ResponseWriter, r *http.Request) {
        if r.URL.Path != "/" {
                http.NotFound(w, r)
                return
        }
        if err := templates.ExecuteTemplate(w, "index.html", nil); err != nil {
                log.Fatal(err)
        }
}

func main() {
        // Register the handlers
        http.HandleFunc("/", indexHandler)

        port := os.Getenv("PORT")
        if port == "" {
                port = "8080"
                log.Printf("Defaulting to port %s", port)
        }

        log.Printf("Listening on port %s", port)
        if err := http.ListenAndServe(":"+port, nil); err != nil {
                log.Fatal(err)
        }
}
