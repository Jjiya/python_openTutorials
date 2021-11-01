<?php require_once("./lib/print.php"); ?>
<h1><a href="practice_php.php">WEB</a></h1>
    <ol>
      <?php
        print_list();
      ?>
    </ol>
    <a href="create.php">create</a>
    <?php
      if(isset($_GET["id"])){
    ?> 
    <a href="update.php?id=<?=$_GET['id']?>&desc=<?=print_description()?>">update</a>
    <?php
      }
    ?>