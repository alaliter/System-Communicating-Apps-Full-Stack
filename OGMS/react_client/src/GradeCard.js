import React from 'react';
import axios from 'axios';

class GradeCard extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      grade: '',
      sid: '',
      year:'',
      term:'',
      crn:''
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({grade: event.target.value});
  }

  handleSubmit(event) {
    alert('You changed the grade of student with ID ' + this.props.info.sid + ' to: ' + this.state.grade);
    event.preventDefault();

    const user = {
      grade: this.state.grade,
      sid: this.props.info.sid,
      term: this.props.info.term,
      year: this.props.info.year,
      crn: this.props.info.crn
    };

    axios.patch(`http://tinman.cs.gsu.edu:5020/request/enrollments/grade/`, user)
      .then(res => {
        console.log(res);
        console.log(res.data);
      })
  }

  render() {
    return(
      <tr>
        <td>{this.props.info.sid}</td>
        <td>{this.props.info.year}</td>
        <td>{this.props.info.term}</td>
        <td>{this.props.info.crn}</td>
        <td>{this.props.info.grade}</td> 
        <td>
          
            <select value={this.state.value} onChange={this.handleChange}>
              <option value="A">A</option>
              <option value="B">B</option>
              <option value="C">C</option>
              <option value="D">D</option>
              <option value="F">F</option>
            </select>

            <button onClick={this.handleSubmit} >submit</button>
          
        </td> 
      </tr>   
    );
  }
}

export default GradeCard;
