<%inherit file="layout.mako"/>
<%block name="home">
    <Label>${user.name} stats:</label><br>
    <div><label>hp: </label> ${user.hp}</div>
    <div><label>mp: </label> ${user.mp}</div>
    <div><label>level: </label> ${user.level}</div>
    <div><label>score: </label> ${user.score}</div>
    <div><label>skills: </label></div>
    % for i in user.skills:
        <div class="row col-xs-12">
            <div class="col-xs-2">${i.name}</div>
            <div class="col-xs-2">mana: ${i.mpc}</div>
            <div class="col-xs-3">damage: ${i.dmg}</div>
        </div>
    % endfor
    <button class="btn btn-primary"><a href="/character">Continue</a></button>
</%block>