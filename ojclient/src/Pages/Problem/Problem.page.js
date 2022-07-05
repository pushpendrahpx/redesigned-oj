import React, { useEffect, useState } from "react";
import { useParams, Navigate, Routes, Route, Router } from "react-router-dom";
import PagetabComponent from "../../Components/Pagetab/Pagetab.component";
import PagebaseMiddleware from "../../Middlewares/Pagebase/Pagebase.middleware";
import APIRoutes from "./../../Utils/APIRoutes.json"
import ProblemHome from "./home/ProblemHome";
import ProblemSubmitPage from "./submit/ProblemSubmit.page";

function ProblemPage (props){
  let [problemState, setProblemState] = useState({})

  let {id} = useParams()

  let fetchProblemById =  async (problemid)=>{
  let response = await fetch(APIRoutes.SERVER_HOST +  APIRoutes.APIS.GET_PROBLEM_BY_ID+problemid, {method:"GET"})
  if(response.ok){
    let jsonResponse = await response.json()

    setProblemState(prev=>{
      return {
        ...prev,
        problem: jsonResponse
      }
    })


  }else{
    alert("Error Loading Problems")
  }
}


  useEffect(()=>{
    console.log(props)
    document.title = 'Problemset - Redesigned OJ'
    fetchProblemById(id)
  },[])

  let problemTabItems = [
    {to: "/problem/" + id +"/", content: 'Problem'  },
    {to:"/problem/" + id + "/submit", content: 'Submit'  },
  ]

  return <PagebaseMiddleware>
          <button className="button" onClick={()=>{
            window.history.go(-1);
          }}>Go Back</button><br /><br />
      <h2 className="title is-5" style={{margin:0}}>{problemState.problem?.title}</h2>

      <PagetabComponent tabItems={problemTabItems} />
    <hr style={{color:"black"}} />

      {/* <div>
        <p style={{padding:"5px"}}>
            {problemState.problem?.description}
        </p>
      </div> */}

      
      <Routes>
        <Route exact path={""} element={<ProblemHome problemDescription={problemState.problem?.description} />} />
        <Route exact path={"submit"} element={<ProblemSubmitPage />} />
      </Routes>
  
      </PagebaseMiddleware>
}



export default (ProblemPage)