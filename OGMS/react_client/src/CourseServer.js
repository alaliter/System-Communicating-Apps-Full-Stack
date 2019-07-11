import React, { Component } from "react";
import CourseCard from './CourseCard';
import axios from 'axios';

const API = 'http://tinman.cs.gsu.edu:5020/request/courses';

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
          <CourseCard info={el} />
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
    return(
      <div>
        <h3>All Courses</h3>
        <table className="table table-striped">
          <thead>
            <tr>
              <th scope="col">Course Number</th>
              <th scope="col">Course Title</th>
              <th scope="col">Course Hour</th>
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