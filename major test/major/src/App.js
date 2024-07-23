import{useEffect, useState} from "react";
import UserData from "./components/UserData";
const API= "http://127.0.0.1:5000/"
const API_ST_XF= "http://localhost:5000/stxf"
const API_ST_XOP= "http://localhost:5000/stxop"
const API_SC_XF= "http://localhost:5000/scxf"
const API_SC_XOP= "http://localhost:5000/scxop"
const API_OBC_XF= "http://localhost:5000/obcxf"
const API_OBC_XOP= "http://localhost:5000/obcxop"
const API_UR_XF= "http://localhost:5000/urxf"
const API_UR_XOP= "http://localhost:5000/urxop"
const App =() => {
  const[Users, setUsers] = useState([]);
  
  const fetchData = () => {
    // Fetch data from /common route
    console.log("hiiii")
    const fetchUsers = async(url)=>
    {
      try{
        const res = await fetch(url);
        const data = await res.json();
        if(data.length >0)
        {
          setUsers(data);
        }
        console.log(data);
      }
      catch(e){
        console.error(e);
      }
    }
    fetchUsers(API);
    // useEffect(() => {
    //   fetchUsers(API1);
    // },[])

  };
  const[Users1, setUsers1] = useState([]);
  const fetchDataSTXF = () => {
    // Fetch data from /common route
    console.log("hiiii")
    const fetchUsers = async(url)=>
    {
      try{
        const res = await fetch(url);
        const data = await res.json();
        if(data.length >0)
        {
          setUsers1(data);
        }
        console.log(data);
      }
      catch(e){
        console.error(e);
      }
    }
    fetchUsers(API_ST_XF);
    // useEffect(() => {
    //   fetchUsers(API1);
    // },[])

  };
  const fetchDataSTXOP = () => {
    // Fetch data from /common route
    console.log("hiiii")
    const fetchUsers = async(url)=>
    {
      try{
        const res = await fetch(url);
        const data = await res.json();
        if(data.length >0)
        {
          setUsers(data);
        }
        console.log(data);
      }
      catch(e){
        console.error(e);
      }
    }
    fetchUsers(API_ST_XOP);
    // useEffect(() => {
    //   fetchUsers(API1);
    // },[])

  };
  const fetchDataSCXF = () => {
    // Fetch data from /common route
    console.log("hiiii")
    const fetchUsers = async(url)=>
    {
      try{
        const res = await fetch(url);
        const data = await res.json();
        if(data.length >0)
        {
          setUsers(data);
        }
        console.log(data);
      }
      catch(e){
        console.error(e);
      }
    }
    fetchUsers(API_SC_XF);
    // useEffect(() => {
    //   fetchUsers(API1);
    // },[])

  };
  const fetchDataSCXOP = () => {
    // Fetch data from /common route
    console.log("hiiii")
    const fetchUsers = async(url)=>
    {
      try{
        const res = await fetch(url);
        const data = await res.json();
        if(data.length >0)
        {
          setUsers(data);
        }
        console.log(data);
      }
      catch(e){
        console.error(e);
      }
    }
    fetchUsers(API_SC_XOP);
    // useEffect(() => {
    //   fetchUsers(API1);
    // },[])

  };
  const fetchDataOBCXF = () => {
    // Fetch data from /common route
    console.log("hiiii")
    const fetchUsers = async(url)=>
    {
      try{
        const res = await fetch(url);
        const data = await res.json();
        if(data.length >0)
        {
          setUsers(data);
        }
        console.log(data);
      }
      catch(e){
        console.error(e);
      }
    }
    fetchUsers(API_OBC_XF);
    // useEffect(() => {
    //   fetchUsers(API1);
    // },[])

  };
  const fetchDataOBCXOP = () => {
    // Fetch data from /common route
    console.log("hiiii")
    const fetchUsers = async(url)=>
    {
      try{
        const res = await fetch(url);
        const data = await res.json();
        if(data.length >0)
        {
          setUsers(data);
        }
        console.log(data);
      }
      catch(e){
        console.error(e);
      }
    }
    fetchUsers(API_OBC_XOP);
    // useEffect(() => {
    //   fetchUsers(API1);
    // },[])

  };
  const fetchDataURXF = () => {
    // Fetch data from /common route
    console.log("hiiii")
    const fetchUsers = async(url)=>
    {
      try{
        const res = await fetch(url);
        const data = await res.json();
        if(data.length >0)
        {
          setUsers(data);
        }
        console.log(data);
      }
      catch(e){
        console.error(e);
      }
    }
    fetchUsers(API_UR_XF);
    // useEffect(() => {
    //   fetchUsers(API1);
    // },[])

  };
  const fetchDataURXOP = () => {
    // Fetch data from /common route
    console.log("hiiii")
    const fetchUsers = async(url)=>
    {
      try{
        const res = await fetch(url);
        const data = await res.json();
        if(data.length >0)
        {
          setUsers(data);
        }
        console.log(data);
      }
      catch(e){
        console.error(e);
      }
    }
    fetchUsers(API_UR_XOP);
    // useEffect(() => {
    //   fetchUsers(API1);
    // },[])

  };
  return<>
  
  <div className="container">
    <h1>SHRI G. S. INSTITUTE OF TECHNOLOGY & SCIENCE, INDORE</h1>
    <h2>Govt. Aided Autonomous Institute Estd. In 1952 | "NIRF Ranked Institute"</h2>
    <h3>Affiliated to Rajiv Gandhi Proudyogiki Vishwavidyalaya, Bhopal & Devi Ahilya Vishwavidyalaya, Indore</h3>
  </div>
  <button onClick={fetchData} >Allotment Result</button>
  <button onClick={fetchDataSTXF} >ST/XF</button>
  <button onClick={fetchDataSTXOP} >ST/XOP</button>
  <button onClick={fetchDataSCXF} >SC/XF</button>
  <button onClick={fetchDataSCXOP} >SC/XOP</button>
  <button onClick={fetchDataOBCXF} >OBC/XF</button>
  <button onClick={fetchDataOBCXOP} >OBC/XOP</button>
  <button onClick={fetchDataURXF} >UR/XF</button>
  <button onClick={fetchDataURXOP} >UR/XOP</button>
  <table>
    <thead>
      <tr>
        <th>Category</th>
        <th>Name</th> 
        <th>CURRENT BRANCH</th> 
        <th>Enrollment No</th>
        <th>Choice1</th>
        <th>Choice2</th>
        <th>Choice3</th>
        <th>Choice4</th>
        <th>Choice5</th>
        <th>Choice6</th>
        <th>Choice7</th>
        <th>Choice8</th>
        <th>Allotment Result</th>
        <th>allotment_status</th>
      </tr>
    </thead>
    <tbody>
      <UserData users= {Users} />
      <UserData users= {Users1} />
    </tbody>
  </table>
  
  </>
}
export default  App;