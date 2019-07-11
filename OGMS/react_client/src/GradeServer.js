import React, { Component } from "react";
import GradeCard from './GradeCard';
import axios from 'axios';

// const API1 = 'http://tinman.cs.gsu.edu:5020/request/enrollments/FA/';
// const API2 = 'http://tinman.cs.gsu.edu:5020/request/enrollments/SU/';
// const API3 = 'http://tinman.cs.gsu.edu:5020/request/enrollments/SP/';
const API = 'http://tinman.cs.gsu.edu:5020/request/enrollments/grade/';
class Grade extends Component {
  constructor(props) {
    super(props);

    this.state = {
      info: [],
    };
  }

  componentDidMount() {
  //   const result = [];   
  //   axios.get(API1)
  //     .then(res1=> { result.fa = res1.data;
  //        axios.get(API2)
  //        .then(res2 => { result.su = res2.data; 
  //          axios.get(API3)
  //          .then(res3 => { result.sp = res3.data;
  //            this.setState({info: [].concat(result.fa, result.su, result.sp)})
  //          })
  //        })
  //     })
  // }
    axios.get(API)
        .then(res => {
          const info = res.data;
          this.setState({ info });
        })
  }
  
  renderInfo() {
    let Info_list = this.state.info.map(function(el) {
      return(
          <GradeCard info={el} />
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
              <th scope="col">Year</th>
              <th scope="col">Term</th>
              <th scope="col">CRN</th>
              <th scope="col">Grade</th>
              <th scope="col">Update</th>
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
 
export default Grade;