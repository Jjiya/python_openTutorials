<?php
    $title = $_POST["title"];
    $desc = $_POST["desc"];
    echo $title;
    echo $desc;
    file_put_contents("data/".$title, $desc);
?>