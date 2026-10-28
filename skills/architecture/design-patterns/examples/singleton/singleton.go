// Singleton pattern in Go.
//
// sync.Once is the standard form: the accessor lazily initializes the
// package-level instance exactly once, safely across goroutines. Prefer
// constructing the config in main and passing it down where feasible;
// package-level singletons make dependencies invisible and tests coupled.

package main

import (
	"fmt"
	"sync"
)

type AppConfig struct {
	settings map[string]string
}

func (c *AppConfig) Get(key string) string {
	return c.settings[key]
}

var (
	instance *AppConfig
	once     sync.Once
)

func GetAppConfig() *AppConfig {
	once.Do(func() {
		// Stands in for reading a config file once.
		fmt.Println("Loading configuration (expensive, happens once)")
		instance = &AppConfig{
			settings: map[string]string{
				"app_name":  "InventoryService",
				"db_url":    "postgres://localhost/inventory",
				"log_level": "INFO",
			},
		}
	})
	return instance
}

func main() {
	a := GetAppConfig()
	b := GetAppConfig()

	fmt.Println("same instance:", a == b)
	fmt.Println("app_name:", a.Get("app_name"))
	fmt.Println("db_url:", b.Get("db_url"))
}
