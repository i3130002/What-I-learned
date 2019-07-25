I had a logger script running for a weak or two, though it generate 10 log file per minute. It ends up impossible to remove them as of this folder grow something like 50K files.

Cpanel file manager (No reponse)

File zilla ftp (Server DC [long wait time])

PHP code :D Worked



`<?php`
`$dir    = './../';`
`$files = scandir($dir);`
`print_r($files);`
`foreach($files as $file){`
    `$file = $dir.$file;`
    `//Make sure that this is a file and not a directory.`
    `if(is_file($file) && pathinfo($file)["extension"]=="txt"){`
        `//Use the unlink function to delete the file.`
        `unlink($file) or die("Couldn't delete file");`
    `}`
`}`
`?>`

