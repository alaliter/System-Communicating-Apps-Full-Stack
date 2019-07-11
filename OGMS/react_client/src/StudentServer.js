import React, { Component } from "react";
import StudentCard from './StudentCard';
import axios from 'axios';

const API = 'http://tinman.cs.gsu.edu:5020/request/students';

class Course extends Component {
  constructor(props) {
    super(props);

    this.state = {
      info: [],
    };
  }

  componentDidMount() {
    fetch(API)
      .then(response => response.json())
      .then(data => this.setState({ info: data }));
  }

  renderInfo() {
    let Info_list = this.state.info.map(function(el) {
      return(
          <StudentCard info={el} />
      );
    });

    return(
      this.state.info.length
      ? Info_list
      : (<div id='msg-app-loading'>
          Loading
        </div>)
    );
  }

  
  render() {
    return (
      <div>
        <h3>All Students</h3>
        <table className="table table-striped">
          <thead>
            <tr>
              <th scope="col">Student ID</th>
              <th scope="col">First Name</th>
              <th scope="col">Last name</th>
              <th scope="col">Email</th>
            </tr>
          </thead>
          <tbody>
              {this.renderInfo()}
          </tbody>
        </table>       
      </div>
    );
  }
}
 
export default Course;