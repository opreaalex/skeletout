package skeleton

import (
	"path/filepath"
	"os"
	"strings"
	"io/ioutil"
	"fmt"

	"github.com/opreaalex/skeletout/utils"
)

const TEMPLATES_DIR_KEY = "templatesDir"
const APP_NAME_KEY  = "appName"
const APP_NAME_REPLACE  = "_app_name_"
const APP_UPPER_NAME_REPLACE  = "_app_upper_name_"
const OUT_DIR_KEY  = "outputDir"
const OUT_DIR_PERM = 0775
const OUT_FILE_PERM = 0644

type Skeleton struct {
	context map[string]string
	files []SkeletonFile
}

type SkeletonFile struct {
	skeleton Skeleton
	isDir bool
	path string
	title string
	content string
}

func CreateSkeleton(ctx map[string]string) Skeleton {
	tpDir := ctx[TEMPLATES_DIR_KEY]
	sk := Skeleton{
		context: ctx,
		files: make([]SkeletonFile, 0, 20),
	}

	filepath.Walk(tpDir, func (path string, info os.FileInfo, err error) error {
		if err != nil { return err }
		if tpDir != path {
			skFile := createSkeletonFile(sk, path, info)
			sk.files = append(sk.files, skFile)
		}
		return nil
	})

	return sk
}

func createSkeletonFile(skeleton Skeleton,
						templatePath string,
						info os.FileInfo) SkeletonFile {
	templatesDir := skeleton.context[TEMPLATES_DIR_KEY]
	baseTemplates := strings.Replace(templatesDir, "./", "", 1)

	base := strings.Replace(templatePath, fmt.Sprintf("%s/", baseTemplates), "", 1)
	path := replaceWithContext(base, skeleton.context)
	title := replaceWithContext(info.Name(), skeleton.context)
	content := ""

	if !info.IsDir() {
		originalContent, err := ioutil.ReadFile(templatePath)
		if err == nil {
			content = replaceWithContext(string(originalContent), skeleton.context)
		}
	}

	return SkeletonFile{
		skeleton: skeleton,
		isDir: info.IsDir(),
		path: path,
		title: title,
		content: content,
	}
}

func replaceWithContext(s string, ctx map[string]string) string {
	appName := ctx[APP_NAME_KEY]
	appUpperName := utils.Capitalize(appName)
	replaced := strings.Replace(s, APP_NAME_REPLACE, appName, -1)
	replaced = strings.Replace(replaced, APP_UPPER_NAME_REPLACE, appUpperName, -1)

	return replaced
}

func (sk *Skeleton) Output() {
	for _, skFile := range sk.files {
		outDir := skFile.ensureOutputDir()
		if !skFile.isDir {
			outPath := fmt.Sprintf("%s/%s", outDir, skFile.title)
			ioutil.WriteFile(outPath, []byte(skFile.content), OUT_FILE_PERM)
		}
	}
}

func (skFile *SkeletonFile) ensureOutputDir() string {
	baseOutDir := skFile.skeleton.context[OUT_DIR_KEY]
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
		outDir = fmt.Sprintf("%s/%s", baseOutDir, fileDir)
	} else {
		outDir = fmt.Sprintf("%s/%s", baseOutDir, skFile.path)
	}

	if _, err := os.Stat(outDir); os.IsNotExist(err) {
		os.MkdirAll(outDir, OUT_DIR_PERM)
	}

	return outDir
}
