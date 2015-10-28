<!DOCTYPE html>
<html lang="no-nb">

<head>
  <!-- <LINK href="http://karsten.pythonanywhere.com/views/flatly.min.css" rel="stylesheet" type="text/css"> -->
  <LINK href="http://bootswatch.com/cosmo/bootstrap.min.css" rel="stylesheet" type="text/css">

</head>

<body>

<div class="navbar navbar-default">
  <div class="navbar-header">
    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-responsive-collapse">
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
    </button>
    <a class="navbar-brand" href="http://karsten.pythonanywhere.com/dangerlevel">Varslingsregion</a>
  </div>
  <div class="navbar-collapse collapse navbar-responsive-collapse">
    <ul class="nav navbar-nav">
      <li class="dropdown">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
        <ul class="dropdown-menu">
          <li><a href="#">Alta</a></li>
          <li><a href="#">K�fjord</a></li>
          <li><a href="#">Lyngen</a></li>
          <li class="divider"></li>
          <li class="dropdown-header">Med flere</li>
          <li><a href="#">...</a></li>
        </ul>
      </li>
    </ul>
    <form class="navbar-form navbar-left">
      <input type="text" class="form-control col-lg-8" placeholder="Search">
    </form>
    <ul class="nav navbar-nav navbar-right">
      <li><a href="#">Link</a></li>
      <li class="dropdown">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
        <ul class="dropdown-menu">
          <li><a href="#">Action</a></li>
          <li><a href="#">Another action</a></li>
          <li><a href="#">Something else here</a></li>
          <li class="divider"></li>
          <li><a href="#">Separated link</a></li>
        </ul>
      </li>
    </ul>
  </div>
</div>


<div class="col-lg-4">

<nav>
  <ul class="pagination">
    <li><a href="#">Oversikt</a></li>
    <li><a href="/test/idag">I dag</a></li>
    <li><a href="#">I morgen</a></li>
    <li><a href="#">Overimorgen</a></li>
    <li><a href="#">Siste 3 d�gn</a></li>
  </ul>
</nav>


{{!base}}

</div>

<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<!-- Include all compiled plugins (below), or include individual files as needed -->
<script src="http://karsten.pythonanywhere.com/views/bower_components/bootstrap/dist/js/bootstrap.min.js"></script>

</body>
</html>