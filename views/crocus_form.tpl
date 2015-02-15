% # template for the form that lets the user choose the region

<div class="row" id="crocus_form">

<div class="btn-group">
  <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
    Velg varslingsregion
    <span class="caret"></span>
  </button>
  <ul class="dropdown-menu" role="menu">
    % for region in region_list:
    <li role="presentation">
        <a href="/crocus/model/{{region}}">{{region}}</a>
    </li>
    % end
  </ul>
</div>

</div>