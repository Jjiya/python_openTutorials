<?php require_once("./lib/print.php"); ?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>PHP</title>
    </head>
  <body>
    <?php require_once("./view/top.php"); ?>
    <form action="update_process.php" method="POST">
      <input type="hidden" name="oldTitle" value="<?=print_title()?>">
      <p><input type="text" name="title" value="<?=print_title()?>"></p>
      <p><textarea name="desc" cols="20" rows="10"><?=print_description()?></textarea></p>
      <input type="submit">
    </form>
  </body>
</html>