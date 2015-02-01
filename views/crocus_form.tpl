% # template for the form that lets the user choose the region

<div class="row" id="crocus_form">

<form action="/region_submit" method="post">
<div class="btn-group">
  <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
    Velg varslingsregion
    <span class="caret"></span>
  </button>
  <ul class="dropdown-menu">
      <div class="input-group">
    % for region in region_list:
    <li role="presentation">
        <input name="region" class="form-control" type="submit" value="{{region}}">
    </li>
    % end
      </div>
  </ul>
</div>
</form>

</div>