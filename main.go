package main

import (
	"fmt"
	"strings"
	"io/ioutil"
	"os"
	"path/filepath"
	"flag"
)

const TEMPLATES_DIR = "./files"

type skeletonFile struct {
	isDir bool
	path string
	title string
	content string
}

func main() {
	appName, outputDir := defineFlags()

	if appName == "" || outputDir == "" {
		flag.PrintDefaults()
		return
	}

	ctx := createContext(appName, outputDir)
	skeleton := createSkeleton(TEMPLATES_DIR, ctx)

	for _, skFile := range skeleton {
		outputSkeletonFile(skFile, ctx)
	}
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

	return ctx
}

func createSkeleton(tpDir string,
					ctx map[string]string) []skeletonFile {

	skeleton := make([]skeletonFile, 0, 20)
	filepath.Walk(tpDir, func (path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if tpDir != path {
			skFile := createSkeletonFile(path, info, ctx)
			skeleton = append(skeleton, skFile)
		}
		return nil
	})
	return skeleton
}

func createSkeletonFile(tpPath string,
						info os.FileInfo,
						ctx map[string]string) skeletonFile {

	// Ignore the path before the templates dir path
	base := strings.Replace(tpPath, "files/", "", 1)
	path := replaceWithContext(base, ctx)
	title := replaceWithContext(info.Name(), ctx)
	content := ""

	if !info.IsDir() {
		origContent, err := ioutil.ReadFile(tpPath)
		if err == nil {
			content = replaceWithContext(string(origContent), ctx)
		}
	}

	return skeletonFile{
		isDir: info.IsDir(),
		path: path,
		title: title,
		content: content,
	}
}

func replaceWithContext(content string, ctx map[string]string) string {
	return strings.Replace(content, "_app_name_", ctx["appName"], -1)
}

func outputSkeletonFile(skFile skeletonFile, ctx map[string]string) {
	outDir := ensureOutputDir(skFile, ctx)
	if !skFile.isDir {
		outPath := fmt.Sprintf("%s/%s", outDir, skFile.title)
		ioutil.WriteFile(outPath, []byte(skFile.content), 0644)
	}
}

func ensureOutputDir(skFile skeletonFile, ctx map[string]string) string {
	var outDir string
	if !skFile.isDir {
		// We need to remove the file name from the file's path
		// This gives us just the directory we must ensure
		var toRemove string
		if strings.Contains(skFile.path, "/") {
			toRemove = fmt.Sprintf("/%s", skFile.title)
		} else {
			toRemove = skFile.title
		}
		fileDir := strings.Replace(skFile.path, toRemove, "", -1)
		outDir = fmt.Sprintf("%s/%s", ctx["outputDir"], fileDir)
	} else {
		outDir = fmt.Sprintf("%s/%s", ctx["outputDir"], skFile.path)
	}

	if _, err := os.Stat(outDir); os.IsNotExist(err) {
		os.MkdirAll(outDir, 0775)
	}

	return outDir
}
