import React, { Component } from "react";
import {
  Route,
  NavLink,
  HashRouter
} from "react-router-dom";
import Home from "./Home";
import Student from "./StudentServer";
import Course from "./CourseServer";
import Enrollment from "./EnrollmentServer";
import Grade from './GradeServer';
import Assistantship from "./AssistantshipServer";
import logo from './logo.jpg';


 class Main extends Component {
  render() {
    return (
      <HashRouter>
        <div className="container">
        <img src={logo} alt="logo" />
          <nav className="navbar navbar-expand-lg navbar-light bg-primary">
            <div className="collapse navbar-collapse" id="navbarNavDropdown">
              <ul className="navbar-nav">
                <li className="nav-item"><NavLink exact to="/"><a className="nav-link">Home</a></NavLink></li>
                <li className="nav-item"><NavLink to="/Student"><a className="nav-link">Student</a></NavLink></li>
                <li className="nav-item"><NavLink to="/Course"><a className="nav-link">Course</a></NavLink></li>     
                <li className="nav-item"><NavLink to="/Enrollment"><a className="nav-link">Enrollment</a></NavLink></li>     
                <li className="nav-item"><NavLink to="/Grade"><a className="nav-link">Grade</a></NavLink></li>     
                <li className="nav-item"><NavLink to="/Assistantship"><a className="nav-link">Assistantship</a></NavLink></li>                   
              </ul>
            </div>
          </nav>

          <div className="content">
            <br/>
            <h2>Welcome to the CSC department!</h2>
            <Route exact path="/" component={Home}/>
            <Route path="/Student" component={Student}/>
            <Route path="/Course" component={Course}/>
            <Route path="/Enrollment" component={Enrollment}/>
            <Route path="/Grade" component={Grade}/>
            <Route path="/Assistantship" component={Assistantship}/>
          </div>

        </div>
      </HashRouter>
    );
  }
}
 
export default Main;