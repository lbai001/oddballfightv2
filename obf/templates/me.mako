<%inherit file="layout.mako"/>
<%block name="home">
    <p>Who do you wish to be?</p>
    <form>
        % for i in characters:
            <input type="radio" name="user" value=${i.id}> ${i.name}<br>
        %endfor
            <input type="submit" value="submit">
    </form>
    % if user:
        <label>${user.name} stats: </label><br>
        <p><label>name :</label> ${user.name}</p>
        <p><label>hp :</label> ${user.hp}</p>
        <p><label>mp :</label> ${user.mp}</p>
    %endif
</%block>