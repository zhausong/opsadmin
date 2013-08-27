<?php
$path = 'sample/'.$_POST['data'];

if(file_exists($path)){
    $file_content = file_get_contents($path);
    echo $file_content;
}
else{
    echo 0;
}
    