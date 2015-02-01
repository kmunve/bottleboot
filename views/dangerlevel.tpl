<!DOCTYPE html>
<html lang="no-nb">

<head>
    <LINK href="http://karsten.pythonanywhere.com/views/journal.css" rel="stylesheet" type="text/css">
    <style> 
      body {
      margin: 0;
      padding-top: 70px;
      }
    </style>
</head>

<body>

<div class="container-fluid">
<div class="col-lg-8">

<p>
<nav class="navbar navbar-default navbar-fixed-top">
  <div class="container">
    
    <div class="btn-group">
      <!-- <button type="button" class="btn btn-default">Velg varslingsregion</button> -->
      <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
	Velg varslingsregion<span class="caret"></span>
      </button>
      <ul class="dropdown-menu">
	% for region in region_list:
	<li><a href="#{{ region }}">{{ region }}</a></li>
	%end

      </ul>
    </div>

  </div>
</nav>

</p>

<p>

% for region in region_list:
<div class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title"><a name="{{ region }}">Utvikling av faregraden i {{ region }}</a></h3>
  </div>
  <div class="panel-body">

    <img src="http://karsten.pythonanywhere.com/media/{{ region }}_thumb.png" height="400" class="img-responsive">
    <br>
    <p align=left>Last ned som <a href="http://karsten.pythonanywhere.com/media/{{ region }}.pdf">PDF</a> eller <a href="http://karsten.pythonanywhere.com/media/{{ region }}.png">bildefil</a>.</p>

  </div>
</div>
% end

</p>

</div>

<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<!-- Include all compiled plugins (below), or include individual files as needed -->
<script src="http://karsten.pythonanywhere.com/views/bower_components/bootstrap/dist/js/bootstrap.min.js"></script>

</div>
</body>
</html>
