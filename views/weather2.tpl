% rebase('base.tpl')

% """Test comment"""

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



