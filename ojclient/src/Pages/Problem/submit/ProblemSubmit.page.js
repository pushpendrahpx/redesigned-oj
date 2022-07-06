import React, { useEffect, useState } from "react";
import { useParams, Navigate } from "react-router-dom";
import PagetabComponent from "../../../Components/Pagetab/Pagetab.component";
import PagebaseMiddleware from "../../../Middlewares/Pagebase/Pagebase.middleware";
import APIRoutes from "./../../../Utils/APIRoutes.json"
let defaultCPPCode = `#include <bits/stdc++.h>
using namespace std;
int main(){
  // Start typing from here..
  return 0;
}`
function ProblemSubmitPage (props){
  let [results,setResults] = useState({output:'',status:'',submission:'',verdict:'',})
  let [sourcecode,setSourcecode] = useState(defaultCPPCode)
  let [problem, setProblem] = useState({})
  useEffect(()=>{
    setProblem(props.problemDetails);
  },[sourcecode])



  useEffect(() => {
    setProblem(props.problemDetails)
    // setSuperCount(count * 2);
  }, [props.problemDetails]);

  

  // On File Change
  let onFileSelect = (e)=>{

    let fr = new FileReader()
    fr.readAsText(e.target.files[0])
    fr.onload = ()=>{
      setSourcecode(fr.result)
    }
    
  }
  // on File uplaod
  let onFileSubmit = (e)=>{
    e.preventDefault()

    // window.alert("SD")
  }



  let onChangeTextArea = (e)=>{
    setSourcecode(prev=>{
      return e.target.value
    })
  }


  // Code submit
  let codeSubmit = async (e)=>{
    e.preventDefault()

    console.log(sourcecode)
    let response = await fetch(APIRoutes.SERVER_HOST + APIRoutes.APIS.SUBMIT_PROBLEM, {
      method:"POST",
      credentials: "include",
      headers:{
        'Content-type':'text/plain',
        'problemcode':problem.problemcode,
        'language':'C++'
      },
      body: sourcecode
    })

    let dataResults = await response.json()
    setResults({
      output:dataResults.output,
      status: dataResults.status,
      submission: dataResults.submission,
      verdict: dataResults.verdict
    })

  }

  return <div>
    <form onSubmit={onFileSubmit} style={{display:"flex"}}>


        <div className="file has-name is-fullwidth">
          <label className="file-label">
            <input onChange={onFileSelect} className="file-input" type="file" name="code" accept=".cpp, .py, .java" />
            <span className="file-cta">
              <span className="file-icon">
                <i className="fas fa-upload"></i>
              </span>
              <span className="file-label">
                Choose a file…
              </span>
            </span>
            <span className="file-name">
              No file Selected
            </span>
          </label>
        </div>


    </form>
    <hr />
    
    <form onSubmit={codeSubmit}>
      <textarea className="textarea" placeholder="Start Coding Here..." rows="10" value={sourcecode} onChange={onChangeTextArea}></textarea>

      <div className="select">
        <select name="language">
          <option value="" disabled>Select language</option>
          <option value="C++">C++</option>
          {/* <option>Python</option> */}
        </select>
      </div>

      <div>
        <button className="button is-link">Submit</button>
      </div>
    </form>


  {/* Output Section */}
  <hr />
    <div>
    <h5 className="title is-5">Output</h5>
    {results.output.length == 0 ? 
      'Please submit to see the output'
    : 
        <><table className="table">
        <tbody>
          <tr><td><b>verdict : </b></td><td> {results.verdict} {results.verdict == 'ACCEPTED' ? '✅' : '❌'}</td></tr>
          <tr><td><b>status : </b></td><td> {results.status} {results.status == 'SUBMITTED' ? '✅' : '❌'} </td></tr>
        </tbody>
      </table>
      <pre>{results.output}</pre></>
    }

    </div>


  </div>
}



export default (ProblemSubmitPage)