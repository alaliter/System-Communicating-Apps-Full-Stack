import React from 'react';
import axios from 'axios';

class AssistantshipCard extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      assistantship: '',
      sid: ''
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({assistantship: event.target.value, sid: event.target.id});
  }

  handleSubmit(event) {
    alert('You changed the assistantship of student with ID ' + this.state.sid + ' to: ' + this.state.assistantship);
    event.preventDefault();

    const user = {
      assistantship: this.state.assistantship,
      sid: this.state.sid
    };

    axios.patch('http://tinman.cs.gsu.edu:5020/student/assistantship/', user)
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
        <td>{this.props.info.assistantship}</td> 
        <td>
          <form onSubmit={this.handleSubmit}>
            <select id={this.props.info.sid} value={this.state.value} onChange={this.handleChange}>
              <option value="Y">Yes</option>
              <option value="N">No</option>
            </select>
            <input type="submit" value="Submit" />
          </form>
        </td> 
      </tr>   
    );
  }
}

export default AssistantshipCard;
