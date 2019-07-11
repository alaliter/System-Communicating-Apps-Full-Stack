import React, { Component } from "react";
import EnrollmentCard from './EnrollmentCard';
import axios from 'axios';

// const API1 = 'http://tinman.cs.gsu.edu:5001/students/enrolled/CSC/FA/';
// const API2 = 'http://tinman.cs.gsu.edu:5001/students/enrolled/CSC/SU/';
// const API3 = 'http://tinman.cs.gsu.edu:5001/students/enrolled/CSC/SP/';
const API1 = 'http://tinman.cs.gsu.edu:5020/request/enrollments/FA/';
const API2 = 'http://tinman.cs.gsu.edu:5020/request/enrollments/SU/';
const API3 = 'http://tinman.cs.gsu.edu:5020/request/enrollments/SP/';

class Course extends Component {
  constructor(props) {
    super(props);

    this.state = {
      info: [],
    };
  }

  componentDidMount() {
    // methold1
    const result = [];   
    axios.get(API1)
      .then(res1=> { result.fa = res1.data;
         axios.get(API2)
         .then(res2 => { result.su = res2.data; 
           axios.get(API3)
           .then(res3 => { result.sp = res3.data;
             this.setState({info: [].concat(result.fa, result.su, result.sp)})
           })
         })
      })
   
    // methold 2
    // const result = [];   
    // axios.get(API1).then(res=> {result.push(...res.data);});
    // axios.get(API2).then(res=> {result.push(...res.data);});
    // axios.get(API3).then(res=> {result.push(...res.data);});
    // this.setState({info: result});
   
    

  }

  renderInfo() {
    let Info_list = this.state.info.map(function(el) {
      return(
          <EnrollmentCard info={el} />
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
              <th scope="col">Student ID</th>
              <th scope="col">Year</th>
              <th scope="col">Term</th>
              <th scope="col">CRN</th>
        
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
