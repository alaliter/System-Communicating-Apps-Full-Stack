import React from 'react';

class EnrollmentCard extends React.Component{
  render() {
    return(
      <tr>
        <td>{this.props.info.sid}</td>
        <td>{this.props.info.year}</td>
        <td>{this.props.info.term}</td> 
        <td>{this.props.info.crn}</td> 
        <td>{this.props.info.grade}</td> 
      </tr>   
    );
  }
}

export default EnrollmentCard;
