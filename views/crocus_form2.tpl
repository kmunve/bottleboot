% # form-action refers to the url extension in bottle_app.py
% # select id refers to the name in request.forms.get('region') in bottle_app.py


 <form action="/region_submit" method="post">
	 <fieldset>
	    <legend>Selecting elements</legend>
	    <p>
	      <label>Velg region</label>
            <select id="region">
                % for region in region_list:
                <option value = "{{ region }}">{{ region }}</option>
                % end
            </select>
        </p>
	  </fieldset>
% # The submit button needs to be inside the form tag
     <p>
         <input type="SUBMIT" value="Velg">
     </p>
 </form>
