import React from 'react'
import ReactDOM from 'react-dom'


class Test extends React.Component {
  render() {
    return <div>{props.map(item => <TestChild
      key={item.pk}
      title={item.name}
      description={item.about}
      username = {item.user.username}
      created_at = {item.created_at}/>)}</div>;

    }
  }

class TestChild extends React.Component {
  render() {
return (
  <div class="card">
    <div class="card-body">

    <h4 class='card-title'>{{props.name}}</h4>
      <h6 class='card-subtitle mb-2 text-muted'>
      by: <a href="{% url 'recipies:by_recipe' username={{props.username}} %}">@{{props.username}}</a>
      <a href="{% url 'recipies:detailview' pk={{props.pk}} %}">{{props.created_at}}</a>
    </h6>
    <p class='card-text'>
      {{props.about}}
    </p>


  </div>

  </div>
  <br>


)



  }
}

ReactDOM.render(
  <Test />,
  window.react_mount
);
