<%inherit file="layout.mako"/>
<%block name="home">
    <form action="/stat">
    <div>
        <p>Who do you wish to be?</p>
        % for i in characters:
            <input type="radio" name="user" value=${i.id} checked> ${i.name}<br>
        %endfor
    </div>
    <input type="submit" value="submit">
    </form>
</%block>