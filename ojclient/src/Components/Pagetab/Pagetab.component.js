import React from "react"
import { Link } from "react-router-dom"

import "./Pagetab.component.css"
function PagetabComponent(props){
    console.log(props)

    return <div className="pagetab-base">
    <div className="page-container">
      <div className="pagetab-tab"> 

          {props.tabItems.map((eachTabItem, eachIndex)=>{
            return <div key={eachIndex}> <Link to={eachTabItem.to}> {eachTabItem.content} </Link> </div>
          })}
          
        </div>
    </div>
  </div>
}
export default PagetabComponent