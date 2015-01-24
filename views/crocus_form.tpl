<form action="/region_submit" method="post">
<div class="btn-group">
  <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
    Velg varslingsregion
    <span class="caret"></span>
  </button>
  <ul class="dropdown-menu">
    % for region in region_list:
    <li><input name="region" class="form-control" type="submit" value="{{region}}"></input></li>
    % end
    <li class="divider"></li>
  </ul>
</div>
</form>