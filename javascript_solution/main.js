
const fs = require('fs');
const path = require('path');

function findFiles(dirPath, fileName, fileType) {
  let fileList = [];

  function findFilesHelper(currentDirPath) {
    const files = fs.readdirSync(currentDirPath);

    for (const file of files) {
      const filePath = path.join(currentDirPath, file);
      const fileStat = fs.statSync(filePath);

      if (fileStat.isDirectory()) {
        findFilesHelper(filePath);
      } else {
        const fileNameMatches = !fileName || file.includes(fileName);
        const fileTypeMatches = !fileType || path.extname(file) === `.${fileType}`;
        if (fileNameMatches && fileTypeMatches) {
          fileList.push(filePath);
        }
      }
    }
  }

  findFilesHelper(dirPath);
  return fileList;
}

function main() {
  const [dirPath, fileName, fileType] = process.argv.slice(2);
  const files = findFiles(dirPath, fileName, fileType);

  for (const file of files) {
    console.log(file);
  }
}

if (require.main === module) {
  main();
}
