package main

import (
	"flag"

	"github.com/opreaalex/skeletout/skeleton"
)

const TEMPLATES_DIR = "./templates"

func main() {
	appName, outputDir := defineFlags()

	if appName == "" || outputDir == "" {
		flag.PrintDefaults()
		return
	}

	ctx := createContext(appName, outputDir)
	sk := skeleton.CreateSkeleton(ctx)

	sk.Output()
}

func defineFlags() (string, string) {
	appNameFlag := flag.String("a", "", "Application name")
	outputFlag := flag.String("o", "", "Output directory")

	flag.Parse()

	return *appNameFlag, *outputFlag
}

func createContext(appName string, outputDir string) map[string]string {
	ctx := make(map[string]string)
	ctx["appName"] = appName
	ctx["outputDir"] = outputDir
	ctx["templatesDir"] = TEMPLATES_DIR

	return ctx
}
