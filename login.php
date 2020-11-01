<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <link rel="stylesheet" href="css/master.css">
    <meta charset="utf-8">
    <title>Login</title>

  </head>
  <body>
    <center>
    <h1>Login</h1>
  <?php

    define('DB_SERVER', 'sql302.epizy.com');
    define('DB_USERNAME', 'epiz_27033647');
    define('DB_PASSWORD', 'h0yFaudpMitWHn');
    session_start();
    $databasename='epiz_27033647_'.$_SESSION['college'];
    define('DB_DATABASE', $databasename);
    $db = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);

    if($_SERVER["REQUEST_METHOD"] == "POST") {
       // username and password sent from form

       $myusername = mysqli_real_escape_string($db,$_POST['username']);
       $mypassword = mysqli_real_escape_string($db,$_POST['password']);

       $sql = "SELECT * FROM users WHERE userid = '$myusername' and password = '$mypassword'";
       $result = mysqli_query($db,$sql);
       $row = mysqli_fetch_array($result);
       $type = $row['type'];
       $_SESSION['type'] = $type;
       $_SESSION['name'] = $row['name'];;
       $_SESSION['login_user'] = $myusername;
       // If result matched $myusername and $mypassword, table row must be 1 row

       if($type=="student") {
          $_SESSION['login_user'] = $myusername;
          header("location: student/spanel.php");
       }
       elseif ($type=="teacher") {
         header("location: teacher/tpanel.php");
       }else {
          $error = "Your Login Name or Password is invalid";
       }
    }

   ?>
    <section>
      <div class="spacer">

      </div>
        <form action="" method="post">
          <input name="username" placeholder="Enter Username" type="text" class="userid" value="" required><br>
          <input name="password" placeholder="Enter Password" type="password" class="password" value="" required><br>
          <input type="submit" class="continue" value="LOGIN"><br>
          <input type="button" class="continue" value="FORGOT PASSWORD"><br>
        </form>
        <div class="spacer">

        </div>
    </section>
  </center>
  </body>
</html>
