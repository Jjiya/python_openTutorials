<?php
    $title = $_POST["title"];
    $desc = $_POST["desc"];
    file_put_contents("./data/".$title, $desc);

    header("Location: /practice_php.php?id=".$title);
?>