<?php
  require_once("./lib/print.php");
?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>PHP</title>
    </head>
  <body>
    <?php require_once("./view/top.php")?>
    <form action="create_process.php">
      <p><input type="text" name="title"></p>
      <p><textarea name="desc" cols="5" rows="10"></textarea></p>
      <input type="submit">
    </form>
  </body>
</html>