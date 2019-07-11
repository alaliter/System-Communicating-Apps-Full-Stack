import React from 'react';

class CourseCard extends React.Component{
  render() {
    return(
        <tr>
          <td>{this.props.info.cno}</td>
          <td>{this.props.info.ctitle}</td>
          <td>{this.props.info.chours}</td> 
        </tr>   
    );
  }
}

export default CourseCard;
