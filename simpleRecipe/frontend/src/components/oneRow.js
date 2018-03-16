import React, { Component } from "react";

class OneRow extends Component {
  render() {
    return (
      <div className='container'>
        <div className='card storyColor'>
          <h3>{this.props.title}</h3>
          <h5>by: {this.props.author}</h5>
          <div className='card-body'>
            {this.props.img != null ?
              <img src={this.props.img} />
              : <img src='/static/images/FoodPlate.png' /> }
          </div>
          <p>{this.props.about}</p>
        </div>
        <br />
      </div>
  );
  }
}

export default OneRow;
