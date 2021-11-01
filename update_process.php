<?php
    $oldTitle = $_POST["oldTitle"];
    $newTitle = $_POST["title"];
    $newDesc = $_POST["desc"];

    $dirPath = "./data/";

    // 파일 명 변경
    rename($dirPath.$oldTitle, $dirPath.$newTitle);
    // 파일 내용 변경
    file_put_contents($dirPath.$newTitle, $newDesc);
    
    header("Location: /practice_php.php?id=".$newTitle);
?>