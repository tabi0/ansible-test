<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset = "UTF-8">
  <title>PHP Test</title>
</head>
<body>
  <form action="test.php" method="get">
  <input type="text" name="comment"/><br/>
  <input type="submit" value="submit">
  </form>

<?php
if(isset($_GET['comment'])){
$comment = $_GET['comment'];
echo $comment;
}
?>

</body>
</html>
