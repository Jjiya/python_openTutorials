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
    <h2>
      <?php
        print_title();
      ?>
    </h2>
    <?php
      print_description();
    ?>
  </body>
</html>