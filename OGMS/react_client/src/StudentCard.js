import React from 'react';

class StudentCard extends React.Component{
  render() {
    return(
      <tr>
        <td>{this.props.info.sid}</td>
        <td>{this.props.info.fname}</td>
        <td>{this.props.info.lname}</td>
        <td>{this.props.info.email}</td> 
      </tr>   
    );
  }
}

export default StudentCard;
