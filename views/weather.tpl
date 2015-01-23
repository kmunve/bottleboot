<!DOCTYPE html>
<html lang="no-nb">

<head>
<LINK href="http://karsten.pythonanywhere.com/views/flatly.css" rel="stylesheet" type="text/css">

<style>
table, th, td
{
border:1px solid black;
padding:5px;
}
table
{
border-spacing:5px;
}
</style>
</head>

<body>

<div class="panel panel-default">
  <div class="panel-body">

<table class="table-hover">
    <tr>
        <th>Parameter</th>
        <th>gjsn.</th>
        <th>min.</th>
        <th>maks</th>
        <th>enhet</th>
    </tr>

    % for p in wplist:
    <tr>
        <td>{{ p.name }}</td>
        <td>{{ p.avg }}</td>
        <td>{{ p.min }}</td>
        <td>{{ p.max }}</td>
        <td>{{ p.unit }}</td>
    </tr>
    % end

</table>

  </div>
</div>

</body>
</html>


